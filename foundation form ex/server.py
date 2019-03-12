import socket

HOST = "127.0.0.1"  
port_number = 65444  

def form_http_response():

    ## http start line
    start_line = "HTTP/1.0 200 OK\n"

    # The extendable list of HTTP headers
    headers = "Content-Type: text/html\n"

    # break between head and body - the neck, if you will.
    end_of_metadata="\n"

    # message payload, or body
    http_body = """
<html>
<body>
<h1>Form game</h1>
<form action="/server.py" method="post">
        <div>
            <label for="color">Favorite color</label>
            <input type="text" id="color" name="favorite color">
        </div>
        
        <div class="button">
                <button type="submit">Send your message</button>
        </div>
    </form>

</body>
</html>
"""
