from .filing import Filing
import xml.etree.ElementTree as ET
from typing import Dict


class Filing_13F(Filing):
    def __init__(self, filing: str):
        super().__init__(filing)

    def __repr__(self):
        ret = f"13F Filings for {self.manager_name}({self.cik})\n" f" Period: {self.period_of_report}\n" f" Reported: {self.signature_date}\n" f" Header of Length: {0}\n".format(len(self.header))
        for key in self.documents:
            ret += " Document ({0}) of Length: {1}\n".format(key, len(self.documents[key]))
        return ret

    def process_information_table(self):
        try:
            document = self.documents["INFORMATION TABLE"]
        except KeyError:
            return False

        xml_doc, ext = self._extract_section(document, "<XML>", "</XML>")
        if len(xml_doc) == 0:
            return False
        root = ET.fromstring(xml_doc)
        namespace = {"ns1": "http://www.sec.gov/edgar/document/thirteenf/informationtable"}
        self.holdings = []
        for child in root:
            try:
                holding = Holding(child, namespace)
                self.holdings.append(holding)
            except ValueError as error:
                print("Error processing Holding:", error)

        return True

    def _process_header_data(self, root: ET.Element, namespace: Dict[str, str]):
        header_data = _get_element(root, "ns1:headerData", namespace)
        filer_info = _get_element(header_data, "ns1:filerInfo", namespace)
        self.period_of_report = _get_element_text(filer_info, "ns1:periodOfReport", namespace)

        filer = _get_element(filer_info, "ns1:filer", namespace)
        creds = _get_element(filer, "ns1:credentials", namespace)
        self.cik = _get_element_text(creds, "ns1:cik", namespace)

    def _process_form_data(self, root: ET.Element, namespace: Dict[str, str]):
        form_data = _get_element(root, "ns1:formData", namespace)
        cover_page = _get_element(form_data, "ns1:coverPage", namespace)
        filing_manager = _get_element(cover_page, "ns1:filingManager", namespace)
        self.manager_name = _get_element_text(filing_manager, "ns1:name", namespace)

        address = _get_element(filing_manager, "ns1:address", namespace)
        self.street1 = _get_element_text(address, "ns2:street1", namespace)
        self.street2 = _get_element_text(address, "ns2:street2", namespace)
        self.city = _get_element_text(address, "ns2:city", namespace)
        self.state_or_country = _get_element_text(address, "ns2:stateOrCountry", namespace)
        self.zip_code = _get_element_text(address, "ns2:zipCode", namespace)

        signature_block = _get_element(form_data, "ns1:signatureBlock", namespace)
        self.signature_date = _get_element_text(signature_block, "ns1:signatureDate", namespace)

    def process_13f_hr(self):
        try:
            document = self.documents["13F-HR"]
        except KeyError:
            return False

        xml_doc, ext = self._extract_section(document, "<XML>", "</XML>")
        if len(xml_doc) == 0:
            return False
        root = ET.fromstring(xml_doc)
        namespace = {"ns1": "http://www.sec.gov/edgar/thirteenffiler", "ns2": "http://www.sec.gov/edgar/common"}
        self._process_header_data(root, namespace)
        self._process_form_data(root, namespace)
        return True


def _get_element(root: ET.Element, path: str, namespace: Dict[str, str]) -> ET.Element:
    x = root.find(path, namespace)
    if x is None:
        raise ValueError(f"During processing of a 13f, the {path} element was not found on the expected parent")
    return x


def _get_element_text(root: ET.Element, path: str, namespace: Dict[str, str], default: str = None):
    x = root.find(path, namespace)
    if x is None:
        if default is None:
            raise ValueError(f"During processing a 13f, the {path} element was not found on the expected parent, thus no .text")
        else:
            return default
    return x.text


class Holding:
    def __init__(self, root: ET.Element, namespace: Dict[str, str]):
        try:
            self.nameOfIssuer = _get_element_text(root, "ns1:nameOfIssuer", namespace, "")
            self.titleOfClass = _get_element_text(root, "ns1:titleOfClass", namespace, "")
            self.cusip = _get_element_text(root, "ns1:cusip", namespace, "")
            self.value = int(float(_get_element_text(root, "ns1:value", namespace, "0"))) * 1000

            shares = root.find("ns1:shrsOrPrnAmt", namespace)

            # not sure if there's a way for additional shares types to be encoded here
            # so we will throw an error if it's not 2
            if shares is None or len(shares) != 2:
                raise ValueError(self.nameOfIssuer + ": shrsOrPrnAmt != 2")

            self.number = int(float(_get_element_text(shares, "ns1:sshPrnamt", namespace, "0")))
            self.type = _get_element_text(shares, "ns1:sshPrnamtType", namespace, "")

        except ValueError:
            raise ValueError(self.nameOfIssuer)
        except AttributeError:
            raise ValueError(self.nameOfIssuer)

    def __repr__(self):
        ret = self.nameOfIssuer + "(${0}:{1} @ {2})".format(self.value, self.number, self.value / self.number)
        return ret


#
# <ns1:informationTable xmlns:ns1="http://www.sec.gov/edgar/document/thirteenf/informationtable">
# 	<ns1:infoTable>
#         <ns1:nameOfIssuer>AMERICAN EXPRESS CO </ns1:nameOfIssuer>
# 		<ns1:titleOfClass>COM</ns1:titleOfClass>
# 		<ns1:cusip>025816109</ns1:cusip>
# 		<ns1:value>27055</ns1:value>
# 		<ns1:shrsOrPrnAmt>
# 			<ns1:sshPrnamt>272430</ns1:sshPrnamt>
# 			<ns1:sshPrnamtType>SH</ns1:sshPrnamtType>
# 		</ns1:shrsOrPrnAmt>
# 		<ns1:investmentDiscretion>SOLE</ns1:investmentDiscretion>
# 		<ns1:votingAuthority>
# 			<ns1:Sole>272430</ns1:Sole>
# 			<ns1:Shared>0</ns1:Shared>
# 			<ns1:None>0</ns1:None>
# 		</ns1:votingAuthority>
# 	</ns1:infoTable>"""
#
