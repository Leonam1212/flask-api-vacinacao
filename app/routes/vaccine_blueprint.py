from flask import Blueprint

from app.controllers.vaccine_controller import insert_vaccine, get_vaccinations

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.post("")(insert_vaccine)
bp_vaccine.get("")(get_vaccinations)