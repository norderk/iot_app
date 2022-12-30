function postData(input) {
    $.ajax({
        type: "POST",
        url: "/reverse_pca.py",
        data: { param: input },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    console.log(response);
}