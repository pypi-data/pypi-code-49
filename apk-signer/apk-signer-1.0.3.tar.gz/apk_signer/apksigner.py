import sys
from zipfile import ZipFile
from pathlib import Path
from subprocess import check_output
from apk_signer import config


def unsign(p_apk):
    if isinstance(p_apk, str):
        raise Exception("p_apk is not str type")

    zip = ZipFile(p_apk)
    for l in zip.namelist():
        if l.startswith('META-INF/'):
            is_signed = True
            break
    else:
        is_signed = False

    if is_signed:
        unsinged_apk_path = str(p_apk.resolve())[:-4] + "-unsigned.apk"
        zout = ZipFile(unsinged_apk_path, 'w')
        for item in zip.infolist():
            buffer = zip.read(item.filename)
            if not item.filename.startswith('META-INF/'):
                zout.writestr(item, buffer)
        zout.close()
        zip.close()
        return Path(unsinged_apk_path)
                
    return p_apk

def apksign(p_apk, key_path: str, key_alias: str, key_pass: str, ks_pass: str):
    try:
        p_apk_name = p_apk.name
        
        kl = ["-zipaligned", "-zipfinal"]
        p_apk_name = p_apk_name.replace("-signed", "-resigned")
        for k in kl:
            if k in p_apk_name:
                if "-resigned" in p_apk_name:
                    p_apk_name = p_apk_name.replace(k, "")
                else:
                    p_apk_name = p_apk_name.replace(k, "-signed")   
                    
        psigned_apk = p_apk.parent.joinpath(p_apk_name)
        key_cmd = ['--ks', key_path, '--ks-key-alias', key_alias, '--ks-pass', 'pass:{}'.format(ks_pass), '--key-pass', 'pass:{}'.format(key_pass)]
        cmd = [config.apksigner, 'sign'] + key_cmd + ['--out', str(psigned_apk.resolve()), str(p_apk.resolve())]
        r = check_output(cmd)
    except Exception as e:
        print("apk signing error: " + str(e))
        return False

    return psigned_apk 

def zipalign(p_apk):
    try:
        base_apk_name = p_apk.name.replace("-unsigned.apk", "")
        if base_apk_name.endswith(".apk"):
            base_apk_name = base_apk_name[:-4]
        
        zipaligned_apk_name = base_apk_name + "-zipaligned.apk"
        p_zipaligned_apk = p_apk.parent.joinpath(zipaligned_apk_name)
        if p_zipaligned_apk.exists():
            p_zipaligned_apk.unlink()

        cmd = [config.zipalign, '-v', '-p', '4', str(p_apk.resolve()), str(p_zipaligned_apk.resolve())]
        r = check_output(cmd)
        return p_zipaligned_apk
    except Exception as e:
        if p_zipaligned_apk.exists():
            try:
                zipfinal_apk_name = base_apk_name + "-zipfinal.apk"
                p_zipfinal_apk = p_apk.parent.joinpath(zipfinal_apk_name)
            
                if p_zipfinal_apk.exists():
                    p_zipfinal_apk.unlink()
                
                cmd = [config.zipalign, '-v', '-p', '4', str(p_zipaligned_apk.resolve()), str(p_zipfinal_apk.resolve())]
                r = check_output(cmd)
                return p_zipfinal_apk
            except Exception as re:
                print("apk re-zipalign error: " + str(re))
                p_zipfinal_apk.unlink()
            finally:
                p_zipaligned_apk.unlink()
        else:
            print("apk zipalign error: " + str(e))
            p_zipaligned_apk.unlink()
            
        return False

def launcher(apk: str, key_path: str, key_alias: str, key_pass: str, ks_pass: str):
    p_apk = Path(apk)
    if not p_apk.exists():
        raise Exception("File not founded: " + str(p_apk.resolve()))

    p_unsigned_apk = unsign(p_apk)
    p_zipaligned_apk = zipalign(p_unsigned_apk)
    if p_zipaligned_apk:
        if p_apk != p_unsigned_apk:
            p_unsigned_apk.unlink()
            
        p_signed_apk = apksign(p_zipaligned_apk, key_path, key_alias, key_pass, ks_pass)
        if p_signed_apk:
            p_zipaligned_apk.unlink()
            apk = str(p_signed_apk.resolve())
            print(apk)
            return apk
