document.getElementById("logout_Button").addEventListener("click", function () {
    fetch("/logout", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => {
            if (response.ok) {
                window.location.href = "/login";
                return response.json();
            }
            throw new Error("Ошибка сети");
        })
        .then((data) => {
            console.log("Успех:", data);
        })
        .catch((error) => {
            console.error("Ошибка:", error);
        });
});
