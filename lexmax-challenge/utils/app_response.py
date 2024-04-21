from flask import Response
import json

class AppResponse():
    def success(self, data, status_code=200):
        res_data = {
            "success": True,
            "data": data
        }
        return Response(
            json.dumps(res_data),
            status=status_code,
            content_type='application/json'
        )
        
    def error(self, error, status_code=500):
        message = error.get("message") if error.get("message") else "Internal server error"
        res_data = {
            "success": False,
            "message": message
        }
        return Response(
            res_data,
            status=status_code,
            content_type='application/json'
        )