function Rate(DishName, rating) {
    fetch('/rate', {
        method: 'POST',
        body: JSON.stringify({ DishName: DishName , rating: rating})
        }).then((_res) => {
            window.location.href = "/";
        });
}