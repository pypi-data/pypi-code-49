import logging

from .reader.factory import PDFReaderFactory, XLSReaderFactory, OFXReaderFactory

logger = logging.getLogger(__name__)


class OFXReaderBR:

    @staticmethod
    def run(files):
        if not files:
            logger.info('No files specified.')
            return

        xls_files = []
        ofx_files = []
        pdf_files = []

        for file in files:
            try:
                if '.xls' in file.filename:
                    xls_files.append(file)
                elif '.pdf' in file.filename:
                    pdf_files.append(file)
                else:
                    ofx_files.append(file)
            except AttributeError:
                if '.xls' in file.name:
                    xls_files.append(file)
                elif '.pdf' in file.name:
                    pdf_files.append(file)
                else:
                    ofx_files.append(file)

        logger.info(ofx_files)
        logger.info(xls_files)
        logger.info(pdf_files)

        # chamar o leitor ofx
        factory_ofx = OFXReaderFactory()
        reader_controller = factory_ofx.create_reader_controller()
        ofx_bank_stmts = reader_controller.read(ofx_files)

        # chamar o leitor xls
        factory_xls = XLSReaderFactory()
        reader_controller = factory_xls.create_reader_controller()
        xls_bank_stmts = reader_controller.read(xls_files)

        # chamar o leitor pdf
        factory_pdf = PDFReaderFactory()
        reader_controller = factory_pdf.create_reader_controller()
        pdf_bank_stmts = reader_controller.read(pdf_files)

        bank_statements = []
        bank_statements.extend(ofx_bank_stmts)
        bank_statements.extend(xls_bank_stmts)
        bank_statements.extend(pdf_bank_stmts)

        logger.info(bank_statements)

        return bank_statements
