var like_counts = new Map()

function on_like_unlike(){
    var post_id = $(this).closest('div').attr('id');
    var like_count = like_counts.get(post_id);
    if($(this).text() == 'like'){
        $.post("/like/",
        {
            post_id: post_id,
            csrfmiddlewaretoken: token,
        }
        );
        $(this).text('unlike');
        like_count += 1;
     }else{
        $.post("/unlike/",
        {
            post_id: post_id,
            csrfmiddlewaretoken: token,
        }
       );
       $(this).text('like');
       like_count -= 1;
    }
    like_counts.set(post_id,like_count);
    $(this).siblings(".like_count").each(set_like_count);
    return false;
}

function set_like_count(){
    $(this).text(like_counts.get($(this).closest('div').attr('id')));
}

$(document).ready(function(){
  $(".like_unlike_button").click(on_like_unlike);
  $(".like_count").each(set_like_count);
});