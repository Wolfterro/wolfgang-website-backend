from django.views.generic import View
from django.http import JsonResponse

from website.models import Info, Block, SocialMedia


# Create your views here.
# =======================
class APIWebsiteView(View):
    def get(self, request, *args, **kwargs):
        info = Info.objects.all().first()
        social_media = SocialMedia.objects.all().first()

        blocks = []
        for block in Block.objects.all().order_by("order"):
            blocks.append(block.get_json())

        return JsonResponse({
            "info": info.get_json(),
            "social_media": social_media.get_json(),
            "blocks": blocks
        })
