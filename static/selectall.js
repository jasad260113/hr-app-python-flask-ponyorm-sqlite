console.log('The selectall.js file works');

document.getElementById('main-checkbox').addEventListener('change',
    function() {
        if(this.checked) {
            selectAllBoxes();
        }
        else {
            deselectAllBoxes();
        }
    }
);

function selectAllBoxes() {
    console.log('The selectAllBoxes function works');
    checkboxes = document.getElementsByName('checkbox');

    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = true;
    }
}

function deselectAllBoxes() {
    console.log('The deselectAllBoxes function works');
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = false;
    }
}
