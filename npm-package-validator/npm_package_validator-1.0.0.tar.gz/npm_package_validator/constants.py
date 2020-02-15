scoped_package_pattern = r"^(?:@([^/]+?)[/])?([^/]+?)$"
blacklist = ["node_modules", "favicon.ico"]

# list of builtin node/js functions
# obtained with
#   > yarn add builtins@latest
#   > import builtins from 'builtins';
#   > console.log(builtins("99999.0.0"))
builtins = [
    "assert",
    "buffer",
    "child_process",
    "cluster",
    "console",
    "constants",
    "crypto",
    "dgram",
    "dns",
    "domain",
    "events",
    "fs",
    "http",
    "https",
    "module",
    "net",
    "os",
    "path",
    "punycode",
    "querystring",
    "readline",
    "repl",
    "stream",
    "string_decoder",
    "sys",
    "timers",
    "tls",
    "tty",
    "url",
    "util",
    "vm",
    "zlib",
    "v8",
    "process",
    "async_hooks",
    "http2",
    "perf_hooks",
]
