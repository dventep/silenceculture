import style_webpage

def web_page(name_button,color_button):
    html = """
        <html>
        <head>
            <title>Cultura del silencio</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!--<meta HTTP-EQUIV='refresh' content='1'>-->
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <link rel="icon" href="data:,">
            <link rel="stylesheet" href="static/style_webpage.css">
            <style></style>
        </head>
        <body>
            <div class="container">
                <section class="container_nav">
                    <ul>
                        <li id="logo_silenceCulture"> </li>
                        <li id="home"><a href="/"> </a></li>
                        <li id="analytics"><a href="/?analytics"> </a></li>
                    </ul>
                </section>
                <section class="container_data">
                    <div id="content_graph">
                        <h1>GRÁFICA DE DATOS</h1>
                        <div id="graph_data">
                            
                        </div>
                    </div>
                </section>
            </div>
            <script>
                console.log("hola");
                let miCanvas = document.getElementById("graph_data").getContext("2d)";
                var chart = new Chart(miCanvas, {
                    type:"bar",
                    data:{
                        labels:["Vino", "Tequila", "Cerveza", "Ron"],
                        datasets:[
                            label:"Mi gráfica de bebidas",
                            backgroundColor:"rgb(0,0,0)",
                            data: [12,39,5,30]
                        ]
                    }
                    
                })
            
            </script>
            
        </body>
        </html>
    """ .format(color_button, name_button)
    return html
