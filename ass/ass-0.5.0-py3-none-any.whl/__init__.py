from . import document


__all__ = ["document", "parse"]

parse = document.Document.parse_file
