from . import decode_bytes, encode_bytes

plain = """
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas et
  egestas tortor. Sed vel augue non tortor viverra placerat eget vitae
  tortor. Fusce vulputate, ligula ut pretium tincidunt, ligula nunc
  faucibus odio, ullamcorper condimentum nulla lorem scelerisque
  velit. Suspendisse bibendum nibh eget neque sollicitudin, id rutrum
  felis malesuada. Curabitur aliquet, nisi id rhoncus viverra, leo
  arcu porttitor leo, sed suscipit felis nunc ut orci. Etiam quis
  blandit odio. Integer in turpis sed elit pellentesque tempus vitae
  eget elit. Nunc vel mollis augue. Vestibulum ultricies quam sit amet
  volutpat scelerisque. Curabitur laoreet at eros in congue. Nunc id
  condimentum sapien. Fusce faucibus risus vel lacus aliquam, ut
  varius orci faucibus. Nunc eu neque aliquet, malesuada orci nec,
  iaculis erat. Donec gravida vehicula purus sit amet lacinia.
  Suspendisse feugiat, sapien et rutrum tempus, felis ligula vulputate
  magna, at varius lacus tortor at nisl.

  Ut in ipsum in mauris ullamcorper consectetur condimentum non ante.
  Nunc aliquet varius malesuada. Fusce nunc augue, fermentum sit amet
  scelerisque vitae, porttitor pretium velit. Duis eget dolor ac felis
  pretium vehicula. Donec bibendum lacinia vehicula. Nulla facilisi.
  Morbi orci justo, dapibus id condimentum vitae, mollis sed nisl.
  Praesent eleifend nisl augue, vitae venenatis ligula tincidunt at.
  Vestibulum tincidunt dolor purus, vitae sagittis ligula vehicula et.
  Nam sodales, nunc id ultrices tristique, erat magna consequat eros,
  vel cursus tellus justo sit amet eros. Vivamus id hendrerit augue,
  at vestibulum nibh. Ut massa nisl, laoreet quis metus id, hendrerit
  posuere erat.
""".encode("utf8")

decoded = decode_bytes(encode_bytes(plain))
assert plain == decoded, "Encode/decode failed"
