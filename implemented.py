"""
Implemented use cases with dependencies injected

https://proofit404.github.io/dependencies/
"""
from dependencies import Injector

from adapters import spreadsheet_adapter
from usecases import convert_data
from services import google_sheets, geocoding
from repositories import csv
from config import settings
from validation import error_collector, composite_validator, RequiredFieldsValidator


class ConvertSpreadsheetData(Injector):
    usecase = convert_data.ConvertSpreadsheetData
    settings = settings.Settings(_env_file="config/.env.example")
    reader = google_sheets.GoogleSheetsReader
    adapter = spreadsheet_adapter.SpreadsheetAdapter
    geocoder = geocoding.GeoCodingProcessor
    error_collector = error_collector.ErrorCollector
    validator = composite_validator.CompositeValidator
    validators = [RequiredFieldsValidator()]
    writer = csv.CSVWriter


class ConvertSpreadsheetDataLocally(ConvertSpreadsheetData):
    settings = settings.Settings(_env_file="config/.env")
