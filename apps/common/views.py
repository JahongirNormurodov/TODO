from rest_framework.response import Response
from rest_framework.views import APIView


class ApiRootView(APIView):
    def get(self, request):
        base_url = request.build_absolute_uri("/api/v1/")
        return Response(
            {
                "message": "Todo DRF API",
                "version": "v1",
                "endpoints": {
                    "folders": f"{base_url}folders/",
                    "categories": f"{base_url}categories/",
                    "tags": f"{base_url}tags/",
                    "labels": f"{base_url}labels/",
                    "todos": f"{base_url}todos/",
                },
            }
        )
