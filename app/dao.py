def load_categories():
    return [{
        'id': 1,
        'name': 'Moblie'
    },{
        'id': 2,
        'name': 'Tablet'
    }]

def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPad',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    },{
        'id': 1,
        'name': 'iPhone',
        'price': 2000000,
        'image': 'https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MT223?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1693248280978'
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products