import os

from app.db.connection.sql_alchemy import SqlAlchemyBuilder
from app.services.planting_service import PlantingService
from flask import current_app
from pathlib import Path
import subprocess


class PlantingCalcAreaController:
    sql_server   = os.getenv('MYSQL_HOST')
    sql_database = os.getenv('MYSQL_DATABASE')
    db_builder = SqlAlchemyBuilder(sql_server, sql_database)
    session_local = db_builder.get_session()

    def get_cultures(self):
        return PlantingService.get_cultures(self.session_local())

    def get_calcs(self):
        return PlantingService.get_calcs(self.session_local())

    def get_formats(self):
        return PlantingService.get_format_types(self.session_local())

    def get_products(self):
        return PlantingService.get_products(self.session_local())

    def get_statistics(self):
        session = self.session_local()

        print(current_app)

        try:
            base_dir = Path(current_app.root_path)
            r_dir = base_dir / "r"
            csv_path = r_dir / 'dados.csv'

            PlantingService.export_calcs_to_csv(session, csv_path)
            result = subprocess.run(
                cwd=r_dir,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {
                    'status': 'error',
                    'detail': f"Erro ao executar R:\n{result.stderr}"
                }

            return {
                'status': 'success',
                'data': result.stdout
            }

        except Exception as e:
            return {
                'status': 'error',
                'detail': str(e)
            }