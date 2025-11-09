from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "safari_secret_key"

# --- Packages Dictionary ---
packages = [
    {
        "id": 1,
        "name": "Serengeti National Park",
        "description": "Home to the Great Migration and Africa's Big Five.",
        "image":"https://www.nationalgeographic.com/content/dam/expeditions/destinations/africa/journeys/Tanzania-Safari-Experience/tanzania-safari-experience-lead-lion-cubs.jpg" ,
        "map": "https://maps.google.com/?q=Serengeti+National+Park+Tanzania"
    },
    {
        "id": 2,
        "name": "Ngorongoro Conservation Area",
        "description": "The breathtaking Ngorongoro Crater and Maasai culture.",
        "image": "https://content-management-files.canva.com/cdn-cgi/image/f=auto,q=70/1fb37206-9bb4-4198-a4ce-f8082eb282f4/sunrise-over-snowcapped-mountains-photo2x.png",
        "map": "https://maps.google.com/?q=Ngorongoro+Crater+Tanzania"
    },
    {
        "id": 3,
        "name": "Tarangire National Park",
        "description": "Famous for elephants and baobab trees.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Tarangine_%2862%29.jpg/1024px-Tarangine_%2862%29.jpg",
        "map":"https://maps.google.com/?q=Tarangire+National+Park+Tanzania"
    },
    {
        "id": 4,
        "name": "Lake Manyara National Park",
        "description": "Home to tree-climbing lions and pink flamingos.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "map":"https://maps.google.com/?q=Lake+Manyara+National+Park+Tanzania"
    },
    {
        "id": 5,
        "name": "Bagamoyo",
        "description": "Historic coastal town with rich Swahili culture.",
        "image":"https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "map":"https://maps.google.com/?q=Bagamoyo+Tanzania"
    },

      {"id":6,"name":"Mount Meru", "price": 750.0,
     "image":"https://images.unsplash.com/photo-1526772662000-3f88f10405ff?auto=format&fit=crop&w=1200&q=80",
     "description":"A dormant volcano near Arusha offering breathtaking views.",
     "map":"https://maps.google.com/?q=Meru+National+Park+Tanzania"
   },

    {"id":7,"name":"Zanzibar", "price": 950.0,
     "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
     "description":"Tropical beaches, historic Stone Town, and spice farms.",
     "map":"https://maps.google.com/?q=Zanzibar+National+Park+Tanzania"
    },

   { "id": 8,
        "name": "Selous/Nyerere National Park",
        "description": "Famous for elephants and baobab trees.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Tarangine_%2862%29.jpg/1024px-Tarangine_%2862%29.jpg",
        "map":"https://maps.google.com/?q=Selous/Nyerere+National+Park+Tanzania"

  },

   {"id":9,
        "name": "Mikumi National Park",
        "description": "Famous for elephants and baobab trees.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Tarangine_%2862%29.jpg/1024px-Tarangine_%2862%29.jpg",
        "map":"https://maps.google.com/?q=Mikumi+National+Park+Tanzania"
}
]

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html', packages=packages)

@app.route('/package/<int:pkg_id>')
def package_detail(pkg_id):
    pkg = next((p for p in packages if p["id"] == pkg_id), None)
    if not pkg:
        flash("Package not found!", "danger")
        return redirect(url_for('index'))
    return render_template('package.html', pkg=pkg)

@app.route('/book/<int:pkg_id>', methods=['GET', 'POST'])
def book(pkg_id):
    pkg = next((p for p in packages if p["id"] == pkg_id), None)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash(f"Booking received for {pkg['name']}. Status: Pending confirmation.", "info")
        return redirect(url_for('booking_confirmation', pkg_id=pkg_id))
    return render_template('book.html', pkg=pkg)

@app.route('/booking_confirmation/<int:pkg_id>')
def booking_confirmation(pkg_id):
    pkg = next((p for p in packages if p["id"] == pkg_id), None)
    return render_template('booking_confirmation.html', pkg=pkg)
@app.route('/contacts', methods=['GET','POST'])
def contacts():
   return render_template('contact.html')

@app.route('/success', methods=['GET','POST'])
def success():
   if request.method == 'POST':
      name = request.form.get('name')
      email = request.form.get('email')
      message = request.form.get('message')
      flash('thank you for contacting us we will reply you soon', 'success')
   return render_template('success.html', name=name, email=email)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
