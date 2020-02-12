import re

FAREWELL_MATCHER = re.compile("|".join([
    r'all the best',
    r'cheers',
    r'degards',
    r'have a nice weekend',
    r'many thanks( (&|and)? kind regards)?',
    r'mit freundlichen grüßen',
    r'sincerely',
    r'speak to you soon',
    r'(thanks|thank you)( for your understanding)?( (&|and))?( (best|kind))?( regards)?( from)?',
    r'(with )?((warm(est)?|kind|best) )?(regards|wishes)',
    r'with my best',
    r'yours',
    r'yours( (faithfully|sincerely|truly|))?',
    r'looking forward to (meeting|hearing from) you',
    r'ta',
    r'best',
    r'take care',
    r'thank you, best wishes',
    r'have a (good|great) day',
    r'kindest regards',
    r'hope to hear from you soon',
    r'thx',
    r'tks',
    r'rgds',
    r'(i )?look forward to catching up'
]))

SIGNATURE_MATCHER = re.compile("|".join([
  r'get outlook for \w+',
  r'sent from \w+( \w+)? (on|for) \w+( \w+)?'
]), flags=re.MULTILINE)

LEGAL_MATCHER = re.compile("|".join([
  r'any and all information contained in this email and/or attachments thereto is confidential',
  r'this transmission is intended solely for the addressee and contains confidential information.',
  r'the content of this email and (its|any) attachments (\(\“the email\”\))? (is|are) confidential',
  r'this message may contain information that is confidential or privileged',
  
  r'sent from my',
  r'this message is intended for the addressee named and can contain',
  r'disclaimer: this email and any attachments are intended only for the addressee named and may contain confidential'
  r'-+ forwarded message -+',
  r'DISCLAIMER: this email and any attachments are intended only for the addressee'
]), flags=re.MULTILINE)
