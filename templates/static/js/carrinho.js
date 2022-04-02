const loadProducts = () => {
    if (typeof window === 'object' && window.localStorage) {
        var data = window.localStorage.getItem('PPminicarts'), today, expires;

        if (data) {
            data = JSON.parse(decodeURIComponent(data));
        }
        console.log(data)
        if (data && data.expires) {
            today = new Date();
            expires = new Date(data.expires);

            if (today > expires) {
                this.destroy();
                return;
            }
        }

        return data;
    }
}