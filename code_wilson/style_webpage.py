def style_webpage():
    return """
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }
        h1 {
            color: #0F3376;
            padding: 2vh;
        }
        p {
            font-size: 1.5rem;
        }
        table {
            margin: auto;            
        }
        td{
            padding: 10px ;
        } 
        .Button {           
            border-radius: 31px;           
            display: inline-block;
            cursor: pointer;
            color: #ffffff;
            font-family: Arial;
            font-size: 17px;
            font-weight: bold;
            font-style: italic;
            padding: 17px 19px;
            text-decoration: none;           
        }
        .ButtonR {
            background-color: #ec4949;            
            border: 6px solid #991f1f;           
            text-shadow: 0px 2px 2px #471e1e;
        }
        .ButtonR:hover {
            background-color: #f51616;
        }

        .Button:active {
            position: relative;
            top: 1px;
        }
        .ButtonG {
            background-color: #49ec56;            
            border: 6px solid #23991f;          
            text-shadow: 0px 2px 2px #1e4723;
        }
        .ButtonG:hover {
            background-color: #29f516;
        }  
        .ButtonB_red {
            background-color: #f51b1b;           
            border: 6px solid #b70505;        
        }
        .ButtonB_red:hover {
            background-color: #d90303;
        } 
        .ButtonB_green {
            background-color: #30fd3b;           
            border: 6px solid #03b70c;        
        }
        .ButtonB_green:hover {
            background-color: #73ef71;
        }
    """
