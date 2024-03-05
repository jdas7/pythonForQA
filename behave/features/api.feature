# comentarios
  Feature: : probar un api
    Scenario: api Rick
      Given que tengo un endpoint "https://rickandmortyapi.com/api/character/"
      And cuento con los siguientes query params "name" y su valor "rick"
      When hago la peticion
      Then visualizo el statuscode
      And me responde el contenido con el nombre "Rick Sanchez"