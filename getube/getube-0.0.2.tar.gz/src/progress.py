from tqdm import tqdm


def set_progress_bar(stream):
    pbar = tqdm(total=stream.filesize)

    def _on_progress(chunk, file_handler, bytes_remaining):
        pbar.update(len(chunk))
        if bytes_remaining == 0:
            pbar.close()
    stream.on_progress = _on_progress
