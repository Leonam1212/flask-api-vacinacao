from http import HTTPStatus
from flask import request, current_app, jsonify
from app.exceptions.check_cpf import CheckCpf
from app.models.vaccine_model import VaccineModel
from sqlalchemy.orm.session import Session
from sqlalchemy import exc


from app.configs.database import db


def insert_vaccine():
    data = request.get_json()

    try:
        data["name"] = data["name"].title()
        data["vaccine_name"] = data["vaccine_name"].title()
        data["health_unit_name"] = data["health_unit_name"].title()

        request_keys = set([keys for keys in data.keys()])
        valid_keys = {"cpf", "name", "vaccine_name", "health_unit_name"}

        difference = request_keys.difference(valid_keys)

        for invalid_key in difference:
            del data[invalid_key]

        if (
            data["cpf"] in data
            and data["name"] in data
            and data["vaccine_name"] in data
            and data["health_unit_name"] in data
        ):
            raise KeyError

        if (
            type(data["cpf"]) is str
            and type(data["name"]) is str
            and type(data["vaccine_name"]) is str
            and type(data["health_unit_name"]) is str
        ):
            ...

        if data["cpf"].isdigit() and len(data["cpf"]) == 11:
            raise CheckCpf

        new_vaccine = VaccineModel(**data)

        current_app.db.session.add(new_vaccine)
        current_app.db.session.commit()

        return jsonify(new_vaccine), HTTPStatus.CREATED

    except exc.IntegrityError:
        return {"msg": "CPF already exists"}, HTTPStatus.CONFLICT
    except CheckCpf:
        return {"error": "Invalid CPF"}, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"msg": "the data must be of type str"}, HTTPStatus.BAD_REQUEST
    except KeyError:
        return {"expected_keys": ["cpf", "name", "vaccine_name", "health_unit_name"]}, HTTPStatus.BAD_REQUEST


def get_vaccinations():
    session: Session = db.session
    base_query = session.query(VaccineModel)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    vaccinations = base_query.order_by(VaccineModel.cpf).paginate(page, per_page)

    return jsonify(vaccinations.items), HTTPStatus.OK


