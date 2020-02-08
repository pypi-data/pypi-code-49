# pylint: disable=invalid-name,bare-except,missing-docstring
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from multiprocessing import Pool, cpu_count
from zlib import crc32

import aamp
from aamp import yaml_util as ay
import byml
from byml import yaml_util as by
import pymsyt
import sarc
from syaz0 import compress  # pylint: diable=no-name-in-module
import yaml
from rstb import ResourceSizeTable, SizeCalculator
from rstb.util import write_rstb

from . import AAMP_EXTS, BYML_EXTS, EXEC_DIR, SARC_EXTS, Path, get_canon_name, guess, is_in_sarc
from .files import STOCK_FILES

RSTB_EXCLUDE_EXTS = ['.pack', '.bgdata', '.txt', '.bgsvdata', '.yml', '.json', '.ps1', '.bak',
                     '.bat', '.ini', '.png', '.bfstm', '.py', '.sh', '.old', '.stera']
RSTB_EXCLUDE_NAMES = ['ActorInfo.product.byml', '.done']


@dataclass
class BuildParams:
    mod: Path
    out: Path
    content: str
    aoc: str
    be: bool
    guess: bool
    verbose: bool
    ch_date: datetime


def _should_rstb(f: Path) -> bool:
    f = f.with_suffix(f.suffix.replace('.s', '.'))
    return f.suffix not in RSTB_EXCLUDE_EXTS and f.name not in RSTB_EXCLUDE_NAMES


def load_rstb(be: bool, file: Path = None) -> ResourceSizeTable:
    table = ResourceSizeTable(b'', be=be)
    if not file:
        ver = 'wiiu' if be else 'switch'
        file = EXEC_DIR / 'data' / ver / 'rstb.json'
    ref_contents = json.loads(file.read_text(), encoding='utf-8')

    def parse_hash(file: str) -> int:
        try:
            return int(file)
        except ValueError:
            return crc32(file.encode('utf8'))

    table.crc32_map = {parse_hash(k): v for k, v in ref_contents['hash_map'].items()}
    table.name_map = {k: v for k, v in ref_contents['name_map'].items()}
    return table


def _get_rstb_val(ext: str, data: bytes, should_guess: bool, be: bool) -> int:
    if not hasattr(_get_rstb_val, 'calc'):
        setattr(_get_rstb_val, 'calc', SizeCalculator())
    val = _get_rstb_val.calc.calculate_file_size_with_ext(data, wiiu=be, ext=ext)  # pylint: disable=no-member
    if val == 0 and should_guess:
        if ext in AAMP_EXTS:
            val = guess.guess_aamp_size(data, ext)
        elif ext in {'.bfres', '.sbfres'}:
            val = guess.guess_bfres_size(data, ext)
    return val


def _copy_file(f: Path, params: BuildParams):
    t = params.out / f.relative_to(params.mod)
    if not t.parent.exists():
        t.parent.mkdir(parents=True, exist_ok=True)
    if is_in_sarc(f):
        shutil.copy(f, t)
    else:
        data = f.read_bytes()
        canon = get_canon_name(f.relative_to(params.mod))
        t.write_bytes(data)
    if f.modified_date() > params.ch_date and _should_rstb(f):
        return {
            canon: _get_rstb_val(t.suffix, data, params.guess, params.be)
        }
    return {}


def _build_byml(f: Path, be: bool):
    # pylint: disable=no-member
    if not hasattr(_build_byml, 'loader'):
        setattr(_build_byml, 'loader', yaml.CSafeLoader)
        by.add_constructors(_build_byml.loader)

    with f.open('r', encoding='utf-8') as bf:
        data = yaml.load(bf, Loader=_build_byml.loader)
    file_bytes = byml.Writer(data, be, version=2).get_bytes()
    return file_bytes


def _build_aamp(f: Path):
    if not hasattr(_build_aamp, 'loader'):
        _build_aamp.loader = yaml.CLoader
        ay.register_constructors(_build_aamp.loader)

    with f.open('r', encoding='utf-8') as af:
        data = yaml.load(af, Loader=_build_aamp.loader)
    file_bytes = aamp.Writer(data).get_bytes()
    return file_bytes


def _build_yml(f: Path, params: BuildParams):
    rv = {}
    try:
        ext = f.with_suffix('').suffix
        t = params.out / f.relative_to(params.mod).with_suffix('')
        if not t.parent.exists():
            t.parent.mkdir(parents=True, exist_ok=True)
        data: bytes
        if ext in BYML_EXTS:
            data = _build_byml(f, params.be)
        elif ext in AAMP_EXTS:
            data = _build_aamp(f)
        t.write_bytes(data if not t.suffix.startswith('.s') else compress(data))
        if f.modified_date() > params.ch_date and _should_rstb(t):
            canon = get_canon_name(t.relative_to(params.out))
            return {
                canon: _get_rstb_val(
                    t.suffix.replace('.s', ''), data, params.guess, params.be
                )
            }
    except Exception as e:  # pylint: disable=broad-except
        print(f'Failed to build {f.relative_to(params.mod).as_posix()}: {e}')
        return {}
    if params.verbose:
        print(f'Built {f.relative_to(params.mod).as_posix()}')
    return rv

LINK_MAP = {
    3293308145: 'AIProgram/*.baiprog',
    2851261459: 'AISchedule/*.baischedule',
    # 110127898: 'AS/*.bas', 'ASList/*.baslist',
    # 1086735552: 'AttClient/*.batcl', 'AttClientList/*.batcllist',
    1767976113: 'Awareness/*.bawareness',
    713857735: 'BoneControl/*.bbonectrl',
    2863165669: 'Chemical/*.bchemical',
    2307148887: 'DamageParam/*.bdmgparam',
    2189637974: 'DropTable/*.bdrop',
    619158934: 'GeneralParamList/*.bgparamlist',
    414149463: 'LifeCondition/*.blifecondition',
    1096753192: 'LOD/*.blod',
    3086518481: 'ModelList/*.bmodellist',
    # 2366604039: 'Physics/*.bphysics',
    # 1223968357: 'ProfileUser',
    1292038778: 'RagdollBlendWeight/*.brgbw',
    # 4022948047: 'RagdollConfig/*.brgconfig', 'RagdollConfigList/*.brgconfiglist',
    1589643025: 'Recipe/*.brecipe',
    2994379201: 'ShopData/*.bshop',
    # 3829750722: 'SlinkUser',
    3926186935: 'UMii/*.bumii',
    # 1712375071: 'XlinkUser'
}

TITLE_ACTORS = [
    'AncientArrow', 'Animal_Insect_A', 'Animal_Insect_B', 'Animal_Insect_F',
    'Animal_Insect_H', 'Animal_Insect_M', 'Animal_Insect_S', 'Animal_Insect_X',
    'Armor_Default_Extra_00', 'Armor_Default_Extra_01', 'BombArrow_A',
    'BrightArrow', 'BrightArrowTP', 'CarryBox', 'DemoXLinkActor',
    'Dm_Npc_Gerudo_HeroSoul_Kago', 'Dm_Npc_Goron_HeroSoul_Kago', 'Dm_Npc_RevivalFairy',
    'Dm_Npc_Rito_HeroSoul_Kago', 'Dm_Npc_Zora_HeroSoul_Kago', 'ElectricArrow',
    'ElectricWaterBall', 'EventCameraRumble', 'EventControllerRumble',
    'EventMessageTransmitter1', 'EventSystemActor', 'Explode', 'Fader', 'FireArrow',
    'FireRodLv1Fire', 'FireRodLv2Fire', 'FireRodLv2FireChild', 'GameROMPlayer',
    'IceArrow', 'IceRodLv1Ice', 'IceRodLv2Ice', 'Item_Conductor', 'Item_Magnetglove',
    'Item_Material_01', 'Item_Material_03', 'Item_Material_07', 'Item_Ore_F', 'NormalArrow',
    'Obj_IceMakerBlock', 'Obj_SupportApp_Wind', 'PlayerShockWave', 'PlayerStole2',
    'RemoteBomb', 'RemoteBomb2', 'RemoteBombCube', 'RemoteBombCube2', 'SceneSoundCtrlTag',
    'SoundTriggerTag', 'TerrainCalcCenterTag', 'ThunderRodLv1Thunder',
    'ThunderRodLv2Thunder', 'ThunderRodLv2ThunderChild', 'WakeBoardRope'
]

def _build_actor(link: Path, params: BuildParams):
    pack = sarc.SARCWriter(be=params.be)
    actor_name = link.stem
    actor = aamp.Reader(link.read_bytes()).parse()
    actor_path = params.out / params.content / 'Actor'
    targets = actor.list('param_root').object('LinkTarget')
    modified = False
    try:
        files = {}
        for p, name in targets.params.items():
            if name == 'Dummy':
                continue
            if p in LINK_MAP:
                path = LINK_MAP[p].replace('*', name)
                files['Actor/' + path] = actor_path / path
            elif p == 110127898: # ASUser
                list_path = actor_path / 'ASList' / f'{name}.baslist'
                aslist_bytes = list_path.read_bytes()
                files[f'Actor/ASList/{name}.baslist'] = list_path
                aslist = aamp.Reader(aslist_bytes).parse()
                for anim in aslist.list('param_root').list('ASDefines').objects.values():
                    filename = anim.param("Filename")
                    if filename != 'Dummy':
                        files[f'Actor/AS/{filename}.bas'] = actor_path / 'AS' / f'{filename}.bas'
            elif p == 1086735552: # AttentionUser
                list_path = actor_path / 'AttClientList' / f'{name}.batcllist'
                atcllist_bytes = list_path.read_bytes()
                files[f'Actor/AttClientList/{name}.batcllist'] = list_path
                atcllist = aamp.Reader(atcllist_bytes).parse()
                for atcl in atcllist.list('param_root').list('AttClients').objects.values():
                    filename = atcl.param('FileName')
                    if filename != 'Dummy':
                        files[f'Actor/AttClient/{filename}.batcl'] = actor_path / 'AttClient' / f'{filename}.batcl'
            elif p == 4022948047: # RgConfigListUser
                list_path = actor_path / 'RagdollConfigList' / f'{name}.brgconfiglist'
                rgconfiglist_bytes = list_path.read_bytes()
                files[f'Actor/RagdollConfigList/{name}.brgconfiglist'] = list_path
                rgconfiglist = aamp.Reader(rgconfiglist_bytes).parse()
                for impl in rgconfiglist.list('param_root').list('ImpulseParamList').objects.values():
                    filename = impl.param('FileName')
                    if filename != 'Dummy':
                        files[f'Actor/RagdollConfig/{filename}.brgconfig'] = actor_path / 'RagdollConfig' / f'{filename}.brgconfig'
            elif p == 2366604039: # PhysicsUser
                phys_source = params.out / params.content / 'Physics'
                phys_path = actor_path / 'Physics' / f'{name}.bphysics'
                phys_bytes = phys_path.read_bytes()
                files[f'Actor/Physics/{name}.bphysics'] = phys_path
                phys = aamp.Reader(phys_bytes).parse()
                types: aamp.ParameterObject = phys.list('param_root').list('ParamSet').objects[1258832850]
                if types.param('use_ragdoll'):
                    rg_path = phys.list('param_root').list('ParamSet').object('Ragdoll').param('ragdoll_setup_file_path')
                    files[f'Physics/Ragdoll/{rg_path}'] = phys_source / 'Ragdoll' / rg_path
                if types.param('use_support_bone'):
                    sb_path = phys.list('param_root').list('ParamSet').object('SupportBone').param('support_bone_setup_file_path')
                    files[f'Physics/SupportBone/{sb_path}'] = phys_source / 'SupportBone' / sb_path
                if types.param('use_cloth'):
                    cloth_path = phys.list('param_root').list('ParamSet').list('Cloth').object('ClothHeader').param('cloth_setup_file_path')
                    files[f'Physics/Cloth/{cloth_path}'] = phys_source / 'Cloth' / cloth_path
                if types.param('use_rigid_body_set_num') > 0:
                    for rigid in phys.list('param_root').list('ParamSet').list('RigidBodySet').lists.values():
                        try:
                            rigid_path = rigid.objects[4288596824].param('setup_file_path')
                            if (phys_path / 'RigidBody' / rigid_path).exists():
                                files[f'Physics/RigidBody/{rigid_path}'] = phys_path / 'RigidBody' / rigid_path
                        except KeyError:
                            continue
        for name, path in files.items():
            if not modified and path.modified_date() > params.ch_date:
                modified = True
            pack.add_file(name, path.read_bytes())
    except FileNotFoundError as e:
        print(f'Failed to build actor "{actor_name}": Could not find linked file "{e.filename}".')
        return {}
    sb = pack.get_bytes()
    dest: Path
    if actor_name in TITLE_ACTORS:
        dest = params.out / params.content / 'Pack' / 'TitleBG.pack' / 'Actor' / 'Pack' / f'{actor_name}.sbactorpack'
    else:
        dest = params.out / params.content / 'Actor' / 'Pack' / f'{actor_name}.sbactorpack'
    if not dest.parent.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(
        compress(sb)
    )
    if modified:
        return {
            f'Actor/Pack/{actor_name}.bactorpack': _get_rstb_val(
                '.sbactorpack', sb, params.guess, params.be
            )
        }
    return {}
    

def _build_sarc(d: Path, params: BuildParams):
    rvs = {}
    for f in {
            f for f in (params.mod / d.relative_to(params.out)).rglob('**/*') if f.is_file()
    }:
        if f.modified_date() > params.ch_date:
            modified = True
            break
    else:
        modified = False
    try:
        s = sarc.SARCWriter(params.be)
        lead = ''
        if (d / '.align').exists():
            alignment = int((d / '.align').read_text())
            s.set_default_alignment(alignment)
            (d / '.align').unlink()
        if (d / '.slash').exists():
            lead = '/'
            (d / '.slash').unlink()

        f: Path
        for f in {f for f in d.rglob('**/*') if f.is_file()}:
            path = f.relative_to(d).as_posix()
            data = f.read_bytes()
            s.add_file(lead + path, data)
            f.unlink()

        shutil.rmtree(d)
        sb = s.get_bytes()
        if modified and _should_rstb(d):
            rvs.update({
                get_canon_name(d.relative_to(params.out)): _get_rstb_val(
                    d.suffix, sb, params.guess, params.be
                )
            })
        d.write_bytes(sb if not (d.suffix.startswith('.s') and d.suffix != '.sarc')
                      else compress(sb))
    except:
        print(f'Failed to build {d.relative_to(params.out).as_posix()}')
        return {}
    else:
        if params.verbose:
            print(f'Built {d.relative_to(params.out).as_posix()}')
        return rvs


def _build_actorinfo(params: BuildParams):
    loader = yaml.CSafeLoader
    by.add_constructors(loader)
    actor_info = {
        'Actors': [],
        'Hashes': []
    }
    for actor in (params.mod / params.content / 'Actor' / 'ActorInfo').glob('*.info.yml'):
        actor_info['Actors'].append(yaml.load(
            actor.read_text(encoding='utf-8'),
            Loader=loader
        ))
    actor_info['Hashes'] = [
        byml.Int(crc) if crc < 2147483648 else byml.UInt(crc) for crc in sorted(
            {crc32(actor['name'].encode('utf8')) for actor in actor_info['Actors']}
        )
    ]
    actor_info['Actors'].sort(
        key=lambda actor: crc32(actor['name'].encode('utf8'))
    )
    info_path = params.out / params.content / 'Actor' / 'ActorInfo.product.sbyml'
    info_path.parent.mkdir(exist_ok=True, parents=True)
    info_path.write_bytes(
        compress(
            byml.Writer(actor_info, be=params.be).get_bytes()
        )
    )


def build_mod(args):
    content = 'content' if args.be else 'atmosphere/titles/01007EF00011E000/romfs'
    aoc = 'aoc' if args.be else 'atmosphere/titles/01007EF00011F001/romfs'
    mod = Path(args.directory)
    if not ((mod / content).exists() or (mod / aoc).exists()):
        print('The specified directory is not valid: no content or aoc folder found')
        exit(1)
    out = mod.with_name(f'{mod.name}_build') if not args.output else Path(args.output)
    if out.exists():
        print('Removing old build...')
        shutil.rmtree(out)

    ch_date = datetime.fromtimestamp(float(
        (mod / '.done').read_text()
    ))
    params = BuildParams(mod=mod, out=out, be=args.be, guess=not args.no_guess,
                         verbose=args.verbose, content=content, aoc=aoc,
                         ch_date=ch_date)

    print('Scanning source files...')
    files = {f for f in mod.rglob('**/*') if f.is_file() and 'ActorInfo' not in f.parts}
    other_files = {f for f in files if f.suffix not in {'.yml', '.msyt'}}
    yml_files = {f for f in files if f.suffix == '.yml'}
    f: Path
    rvs = {}

    print('Copying miscellaneous files...')
    if args.single or len(other_files) < 2:
        for f in other_files:
            rvs.update(_copy_file(f, params))
    else:
        p = Pool(cpu_count())
        results = p.map(partial(_copy_file, params=params), other_files)
        for r in results:
            rvs.update(r)

    if (mod / content).exists():
        print('Building actor info...')
        if (mod / content / 'Actor' / 'ActorInfo').is_dir():
            _build_actorinfo(params)

        msg_dirs = {d for d in mod.glob(f'{content}/Pack/Bootup_*.pack')
                    if d.is_dir() and not d.name == 'Bootup_Graphics.pack'}
        if msg_dirs:
            print('Building MSBT files...')
        for d in msg_dirs:
            msg_dir = next(d.glob('Message/*'))
            new_dir = out / msg_dir.relative_to(mod).with_suffix('.ssarc.ssarc')
            pymsyt.create(msg_dir, new_dir)

    print('Building AAMP and BYML files...')
    if args.single or len(yml_files) < 2:
        for f in yml_files:
            rvs.update(_build_yml(f, params))
    else:
        results = p.map(partial(_build_yml, params=params), yml_files)
        for r in results:
            rvs.update(r)

    actors = {f for f in (out / content / 'Actor' / 'ActorLink').glob('*.bxml')}
    if actors:
        (out / content / 'Actor' / 'Pack').mkdir(parents=True, exist_ok=True)
        print('Building actor packs...')
        if args.single or len(actors) < 2:
            for a in actors:
                rvs.update(
                    _build_actor(a, params)
                )
        else:
            results = p.map(partial(_build_actor, params=params), actors)
            for r in results:
                rvs.update(r)
    for d in (out / content / 'Physics').glob('*'):
        if d.stem not in ['StaticCompound', 'TeraMeshRigidBody']:
            shutil.rmtree(d)
    {shutil.rmtree(d) for d in (out / content / 'Actor').glob('*') if d.is_dir() and d.stem != 'Pack'}
        

    print('Building SARC files...')
    dirs = {d for d in out.rglob('**/*') if d.is_dir()}
    sarc_folders = {d for d in dirs if d.suffix in SARC_EXTS and d.suffix != '.pack'}
    pack_folders = {d for d in dirs if d.suffix == '.pack'}
    if args.single or (len(sarc_folders) + len(pack_folders)) < 3:
        for d in sarc_folders:
            rvs.update(_build_sarc(d, params))
        for d in pack_folders:
            rvs.update(_build_sarc(d, params))
    else:
        sarc_func = partial(_build_sarc, params=params)
        results = p.map(sarc_func, sarc_folders)
        for r in results:
            rvs.update(r)
        results = p.map(sarc_func, pack_folders)
        for r in results:
            rvs.update(r)

    rp = out / content / 'System' / 'Resource' / 'ResourceSizeTable.product.json'
    if rp.exists() or rvs:
        print('Updating RSTB...')
        table: ResourceSizeTable
        if args.no_rstb:
            if rp.exists():
                table = load_rstb(args.be, file=rp)
        else:
            if rp.exists():
                table = load_rstb(args.be, file=rp)
            else:
                table = load_rstb(args.be)
                rp.parent.mkdir(parents=True, exist_ok=True)
            if rvs and not (len(rvs) == 1 and list(rvs.keys())[0] is None):
                for p, v in rvs.items():
                    if not p:
                        continue
                    msg: str = ''
                    if table.is_in_table(p):
                        if v > table.get_size(p) > 0:
                            table.set_size(p, v)
                            msg = f'Updated {p} to {v}'
                        elif v == 0:
                            table.delete_entry(p)
                            msg = f'Deleted {p}'
                        else:
                            msg = f'Skipped {p}'
                    else:
                        if v > 0 and p not in STOCK_FILES:
                            table.set_size(p, v)
                            msg = f'Added {p}, set to {v}'
                    if args.verbose and msg:
                        print(msg)
        write_rstb(table, str(rp.with_suffix('.srsizetable')), args.be)
        if rp.exists():
            rp.unlink()

    print('Mod built successfully')
