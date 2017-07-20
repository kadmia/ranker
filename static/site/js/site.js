$(document).ready(
    $("article.message button.delete").click(function()
    {$(this).parents("article.message").addClass("is-hidden");
    })
);