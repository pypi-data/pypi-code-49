import logging
import os
from typing import Text

from sanic import Blueprint, response
from sanic.exceptions import NotFound
from sanic.request import Request
from sanic.response import text
import aiofiles
import ragex.community
import ragex.community.utils as rasa_x_utils

from rasa.cli.utils import print_success, print_info, print_error
from ragex.community import utils, config, constants

logger = logging.getLogger(__name__)

image_dir = os.path.abspath(config.rasa_image_dir)


async def write_file(path, body):
    async with aiofiles.open(path, 'wb') as f:
        await f.write(body)
    f.close()

def valid_file_size(file_body):
    if len(file_body) < 50485760:
        return True
    return False

def valid_file_type(file_name, file_type):
    file_name_type = file_name.split('.')[-1]
    if file_name_type in ["png", "gif", "jpg"] and file_type in [ "image/jpeg", "image/gif", "image/png"]:
        return True
    return False


def blueprint() -> Blueprint:
    """ Serve image """

    print_info(f"image_dir:{image_dir}")

    images = Blueprint("images", url_prefix="/image")

    images.static("/", image_dir)

    """ upload 요청 처리 """

    @images.route("/projects/<project_id>/upload_image", methods=["POST"])
    async def upload_image(request, project_id):
        # print_info(request.files)
        try:

            upload_file = request.files.get('file')

            if not upload_file:
                raise ValueError

            filename= utils.secure_filename(upload_file.name)

            if not valid_file_type(upload_file.name, upload_file.type):
                return rasa_x_utils.error(
                    404,
                    "ImageUploadTypeError",
                    "Image file type not valid"
                )

            if not valid_file_size(upload_file.body):
                return rasa_x_utils.error(
                    404,
                    "ImageUploadSizeError",
                    "Image file size not valid (must size under 50485760 ) "
                )

            file_path = f"{image_dir}/{filename}"
            await write_file(file_path, upload_file.body)
            print_success(f"image file upload success:{filename}")
            return response.json({"filename": filename})

        except(FileNotFoundError, ValueError) as e:
            return rasa_x_utils.error(
                404,
                "ImageUploadError",
                "Image upload exception"
            )
        # print_info(f"request image upload files:{rfiles}")




    # class ImageUploadAPI(HTTPMethodView):
    #     async def post(self, request):
    #         access_token = get_token_from_header(request.headers)
    #         token = decode_token(access_token)
    #         user_id = token.get('sub')
    #         upload_file = request.files.get('image')
    #         log_path = os.path.join(os.getcwd(), 'pictures')
    #         if not os.path.exists(log_path):
    #             os.makedirs(log_path)
    #
    #         if not upload_file:
    #             res = {'status': 'no file uploaded'}
    #             return json(res, status=404)
    #
    #         # if not valid_file_type(upload_file.name, upload_file.type):
    #         #     res = {'status': 'invalid file type'}
    #         #     return json(res, status=400)
    #         elif not valid_file_size(upload_file.body):
    #             res = {'status': 'invalid file size'}
    #             return json(res, status=400)
    #         else:
    #             file_path = f"{log_path}/{str(datetime.now())}.{upload_file.name.split('.')[1]}"
    #             await write_file(file_path, upload_file.body)
    #             await apps.db.users.update_one({'_id': ObjectId(user_id)}, {"$set": {
    #                 "nid_front": upload_file.name
    #             }})
    #             return json({'status': 'image uploaded successfully'})

    return images
