import vt


def is_red_scan(file_hash, api_key):
    """
    Check if a file is malicious using VirusTotal API.
    
    Args:
        file_hash (str): The SHA-256 hash of the file
        api_key (str): VirusTotal API key
        
    Returns:
        bool: True if file is malicious, False otherwise
    """
    client = vt.Client(api_key)
    try:
        file = client.get_object(f"/files/{file_hash}")
        stats = file.last_analysis_stats
        # Consider file malicious if it has any malicious verdicts
        is_malicious = stats.get('malicious', 0) > 0
        client.close()
        return is_malicious
    except Exception as e:
        client.close()
        raise e
