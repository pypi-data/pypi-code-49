import os
import uuid

GOOGLE_CLOUD_DIRECTORY_PAYMENT = "payment_slips"
GOOGLE_CLOUD_DIRECTORY_PROOF = "proofs_of_product"
GOOGLE_CLOUD_DIRECTORY_IMAGES = "images"

class FileUtils:
    @staticmethod
    def generate_filename(filename):
      ext = filename.split('.')[-1]
      filename = "%s.%s" % (uuid.uuid4(), ext)
      return filename

    @staticmethod
    def upload_to_images(instance, filename):
      filename = FileUtils.generate_filename(filename)
      return os.path.join(GOOGLE_CLOUD_DIRECTORY_IMAGES, filename)

    @staticmethod
    def upload_to_payment(instance, filename):
      filename = FileUtils.generate_filename(filename)
      return os.path.join(GOOGLE_CLOUD_DIRECTORY_PAYMENT, filename)

    @staticmethod
    def upload_to_proof(instance, filename):
      filename = FileUtils.generate_filename(filename)
      return os.path.join(GOOGLE_CLOUD_DIRECTORY_PROOF, filename)      