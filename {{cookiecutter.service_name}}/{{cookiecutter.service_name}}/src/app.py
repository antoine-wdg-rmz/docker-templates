from eve import Eve


app = Eve()

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
