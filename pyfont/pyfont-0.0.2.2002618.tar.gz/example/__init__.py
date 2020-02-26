if __name__ == '__main__':
    from pyfont import EffectFont, FontFactory

    font = EffectFont()
    path = '../simkai.ttf'
    import os

    print(os.path.abspath(path))
    font.set_text_base(size=100, path=path)
    font.base.clear_margin = True
    # font.shadow((80, 31, 191, 0.3), sigma=8, x=0, y=6)
    # font.gradient([("#da7eeb", 0), ("#9070d8", 0.5)], angle="center", type="radial")
    # font.fill_color = "#da7eeb"
    font.fill_color = (1, 1, 1, 255)
    # font.stroke("#4e1269", 1)
    font.text = '实例\n中国\n实例'
    obj = FontFactory(font, render_by_mixed=True)
    img = obj.render_to_rng()
    print(img.size)
    img.save("11.png")
