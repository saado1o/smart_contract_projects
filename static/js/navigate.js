function navigateToPage() {
    const memberType = document.getElementById("memberType").value.trim(); // Trim the value to remove extra spaces

    if (!memberType) {
        alert('Please select a valid member type.');
        return;
    }

    switch (memberType) {
        case "supplier":
            window.location.href = "/add_supplier";
            break;
        case "manufacturer":
            window.location.href = "/add_manufacturer";
            break;
        case "buyer":
            window.location.href = "/add_buyer";
            break;
        default:
            alert('Invalid member type selected.');
            break;
    }
}
