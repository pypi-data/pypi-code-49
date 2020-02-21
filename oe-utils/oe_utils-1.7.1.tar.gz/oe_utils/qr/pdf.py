import json
from io import BytesIO

from reportlab.graphics import renderPDF
from reportlab.graphics import shapes
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus.paragraph import Paragraph


class QrPdf(object):
    def __init__(
        self,
        request,
        id,
        onderwerp,
        base_url,
        route,
        uri,
        form_data,
        pagesize=A4,
        qr_size=5 * cm,
    ):
        super(QrPdf, self).__init__()
        self.request = request
        self.pagesize = pagesize
        self.qr_size = qr_size
        self.id = id
        self.onderwerp = onderwerp
        self.form_data = form_data
        self.route = route
        self.base_url = base_url
        self.uri = uri

    def generate_pdf(self):
        in_memory_file = BytesIO()
        canvas = Canvas(in_memory_file, pagesize=self.pagesize)
        self._add_text(canvas)
        self._add_qr_code(canvas)
        canvas.save()
        in_memory_file.seek(0)
        return in_memory_file

    def _add_text(self, canvas):
        width, height = self.pagesize
        text = ("Onderwerp: {subject}<br/>URI: {uri}"
                .format(subject=self.onderwerp, uri=self.uri))
        style = ParagraphStyle('Normal')
        style.fontName = 'Courier'
        paragraph = Paragraph(text, style)
        paragraph.wrap(width - (4 * cm), 10 * cm)  # required to wrap before draw
        paragraph.drawOn(canvas, 2 * cm, height - 2 * cm)  # height 0 is the bottom

    def _add_qr_code(self, canvas):
        width, height = self.pagesize
        url = self.base_url + self.request.route_path(self.route, id=self.id)
        qr_data = json.dumps({"url": url, "form_data": self.form_data})

        drawing = shapes.Drawing()
        qr = QrCodeWidget(value=qr_data, barHeight=self.qr_size, barWidth=self.qr_size)
        drawing.add(qr)
        renderPDF.draw(
            drawing, canvas, width / 2 - self.qr_size / 2, height / 2 - self.qr_size / 2
        )
