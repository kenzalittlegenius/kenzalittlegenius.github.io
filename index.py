import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = <!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title class="titre2"> </title>

    <!-- CSS Libraries -->
    <!-- ================================= -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Roboto:200,300,400,700"
    />

    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />

    <!-- My CSS -->
    <!-- ================================= -->
    <link rel="stylesheet" href="css/normalize.css" />
    <link rel="stylesheet" href="css/styles.css" />
    <link rel="stylesheet" type="text/css" href="slick/slick.css" />
    <!-- carousel -->
    <link rel="stylesheet" type="text/css" href="slick/slick-theme.css" />
    <!-- carousel -->
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css"
    />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet" />

    <!-- JS Libraries -->
    <!-- ================================= -->
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
      crossorigin="anonymous"
    ></script>
    <script
      src="http://code.jquery.com/jquery-3.3.1.min.js"
      integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
      crossorigin="anonymous"
    ></script>

    <!-- My Scripts -->
    <script src="./js/scripts.js"></script>
    <script src="./js/_data_.js"></script>
    <script type="text/javascript" src="slick/slick.min.js"></script>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
      <!-- Custom styles for this template -->
      <link href="./Cover_files/cover.css" rel="stylesheet">
<head>
    <body class="text-center">
        <form action="/index.py" method="post">
            <input type="text" name="name" value="Votre nom" />
            <input type="submit" name="send" value="Envoyer information au serveur">
        </form> 
      <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
        <header class="masthead mb-auto">
          <div class="inner">
            <h3 class="masthead-brand">Kenza</h3>
            <nav class="nav nav-masthead justify-content-center">
              <a
                class="nav-link active"
                href="https://google.com"
                >Home</a
              >
              <a
                class="nav-link"
                href="https://google.com"
                >Curriculum</a
              >
              <a
                class="nav-link"
                href="https://google.com"
                >Contact</a
              >
            </nav>
          </div>
        </header>

        <main role="main" class="inner cover">
          <h1  class="cover-heading">Kenza Benmansour</h1>
          <p class="lead">
              Hi, I'm Kenza
          </p>

        </main>

        <footer class="mastfoot mt-auto">
          <div class="inner">

          </div>
        </footer>
      </div>
    </body>
  </head>
</html>
print(html)