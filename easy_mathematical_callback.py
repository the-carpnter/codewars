def process_array(arr, callback):
    return [callback(arr[0])] + process_array(arr[1:], callback) if arr else []
