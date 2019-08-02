var like_counts = new Map()

function get_post_id(){
    return $(this).closest('.post').attr('id');
}

function on_like_unlike(){
    var post_id = get_post_id.call(this);
    var like_count = like_counts.get(post_id);
    var post_id_num = post_id.split('_')[1];
    if($(this).text().trim() == 'like'){
        $.post("/like/",
        {
            post_id: post_id_num,
            csrfmiddlewaretoken: token,
        }
        );
        $(this).text('unlike');
        like_count += 1;
     }else{
        $.post("/unlike/",
        {
            post_id: post_id_num,
            csrfmiddlewaretoken: token,
        }
       );
       $(this).text('like');
       like_count -= 1;
    }
    like_counts.set(post_id,like_count);
    $(this).parent().siblings(".like_count").each(set_like_count);
    return false;
}

function set_like_count(){
    var post_id = get_post_id.call(this);
    var like_count = like_counts.get(post_id);
    var like_text = like_count.toString();
    if(like_count == 1){
        like_text += " like";
    }else{
        like_text += " likes";
    }
    $(this).text(like_text);
}

$(document).ready(function(){
  $(".like_unlike_button").click(on_like_unlike);
  $(".like_count").each(set_like_count);
});