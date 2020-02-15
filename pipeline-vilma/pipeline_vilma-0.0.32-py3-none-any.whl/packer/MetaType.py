class MetaType:
    IMAGE_BASE64 = 'image-base64'
    IMAGE_URL = 'image-url'
    HEATMAP = 'heatmap'
    ENVIRONMENT = 'environment'
    AIR_QUALITY = 'airQuality'
    TEXT = 'text'

    @staticmethod
    def get_file_type(data_type):
        if data_type == MetaType.IMAGE_BASE64:
            return 'jpeg'
        elif data_type == MetaType.IMAGE_URL:
            return 'jpeg'
        elif data_type == MetaType.HEATMAP:
            return 'jpeg'
        elif data_type == MetaType.ENVIRONMENT:
            return 'json'
        elif data_type == MetaType.AIR_QUALITY:
            return 'json'
        elif data_type == MetaType.TEXT:
            return 'json'
