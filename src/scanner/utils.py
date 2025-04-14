import os, stat

#checks for file extensions written right to left
def isrtlext(file):
    rtl_override_present = False
    for char in file:
        if ord(char) == 0x202E: #if file name contains right to left unicode
            rtl_override_present = True
            break
    return rtl_override_present

def get_file_permissions(file_path):
    # Get file mode
    mode = os.stat(file_path).st_mode

    # Define permission symbols
    is_dir = 'd' if stat.S_ISDIR(mode) else '-'
    user_perms = (
        'r' if mode & stat.S_IRUSR else '-',
        'w' if mode & stat.S_IWUSR else '-',
        'x' if mode & stat.S_IXUSR else '-'
    )
    group_perms = (
        'r' if mode & stat.S_IRGRP else '-',
        'w' if mode & stat.S_IWGRP else '-',
        'x' if mode & stat.S_IXGRP else '-'
    )
    other_perms = (
        'r' if mode & stat.S_IROTH else '-',
        'w' if mode & stat.S_IWOTH else '-',
        'x' if mode & stat.S_IXOTH else '-'
    )

    # Combine all permissions
    perms = is_dir + ''.join(user_perms) + ''.join(group_perms) + ''.join(other_perms)
    return perms

def get_metadata(file_path):
    metadata = {}
    metadata['name'] = os.path.basename(file_path)
    metadata['path'] = file_path
    metadata['permissions'] = get_file_permissions(file_path)
    metadata['size'] = os.path.getsize(file_path)
    metadata['last_modified'] = os.path.getmtime(file_path)
    metadata['created'] = os.path.getctime(file_path)
    metadata['last_accessed'] = os.path.getatime(file_path)
    metadata['is_dir'] = os.path.isdir(file_path)
    metadata['is_file'] = os.path.isfile(file_path)
    metadata['is_symlink'] = os.path.islink(file_path)
    return metadata