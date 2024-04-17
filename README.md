

### Hydration party 
* Start the server
    ```bash
    python3 service.py
    ```
    
* Open a new terminal session and to run a JMeter script from the command line
    ```bash
    jmeter -n -t thirsty.jmx
    ```

* Switch back to the tab where you are running the server. You should see the "thirsty song" printed out on your console.
    <pre>
        There are 2 bottles of Brandy in the cabinet. Date=1713344734810 Thread=6
        127.0.0.1 - - [17/Apr/2024 14:35:34] "POST /flask HTTP/1.1" 200 -
         There are 1 bottle of Brandy in the cabinet. Date=1713344734821 Thread=6
        127.0.0.1 - - [17/Apr/2024 14:35:34] "POST /flask HTTP/1.1" 200 -
         There are 0 bottles of Vodka in the cabinet. Date=1713344734830 Thread=6
        127.0.0.1 - - [17/Apr/2024 14:35:34] "POST /flask HTTP/1.1" 200 -
         There are 7 bottles of Whiskey in the cabinet. Date=1713344734847 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:34] "POST /flask HTTP/1.1" 200 -
         There are 1 bottle of Rum in the cabinet. Date=1713344735702 Thread=4
        127.0.0.1 - - [17/Apr/2024 14:35:35] "POST /flask HTTP/1.1" 200 -
         There are 6 bottles of Vodka in the cabinet. Date=1713344735854 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:35] "POST /flask HTTP/1.1" 200 -
         There are 0 bottles of Rum in the cabinet. Date=1713344736716 Thread=4
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 5 bottles of Vodka in the cabinet. Date=1713344736859 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 4 bottles of Brandy in the cabinet. Date=1713344736864 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 3 bottles of Rum in the cabinet. Date=1713344736867 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 2 bottles of Rum in the cabinet. Date=1713344736871 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 1 bottle of Brandy in the cabinet. Date=1713344736877 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
         There are 0 bottles of Whiskey in the cabinet. Date=1713344736881 Thread=7
        127.0.0.1 - - [17/Apr/2024 14:35:36] "POST /flask HTTP/1.1" 200 -
    </pre>
