function Rate(DishName, rating) {
    fetch('/rate', {
        method: 'POST',
        body: JSON.stringify({ DishName: DishName , rating: rating})
        });
}
function onlyOne(checkbox) {
    var checkboxes = document.getElementsByName(checkbox.name)
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}

function EditD(id){
    session['edit'] = id;
    console.log(id);
    window.location.href = "/";
}