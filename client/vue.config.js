module.exports = {
    assetsDir: 'static', // For simple configuration of static files in Flask (the "static_folder='client/dist/static'" part in app.py)
    devServer: {
        proxy: 'http://127.0.0.1:5000/' // So that the client dev server can access your Flask routes
    }
};