$(document).ready(function(){
  $("#id_tags").autocomplete(
      '/ajax/tag/autocomple/',
      {multiple:true,multipleSeparator: ' '}
      );
     });
