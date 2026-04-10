from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


def get_bot_response(user_input):
    if not user_input:
        return "I didn't hear anything!"

    user_input = user_input.strip().lower()

    if user_input in ("exit", "quit", "bye", "goodbye"):
        return "Thank you for using Grand Horizon Hotel. Have a great day!"

    # ─── ROOM BOOKING ────────────────────────────
    elif "book" in user_input and "room" in user_input:
        return "To book a room, please visit our website or call +1-800-HORIZON. Rooms available: Deluxe, Suite, and Standard. What type of room are you interested in?"

    elif "check-in" in user_input or "check in" in user_input:
        return "Standard check-in time is 2:00 PM. Early check-in (from 11 AM) is available for an extra charge of $30."

    elif "check-out" in user_input or "check out" in user_input:
        return "Standard check-out time is 11:00 AM. Late check-out (until 2 PM) can be arranged for an extra $25."

    elif "cancel" in user_input and ("booking" in user_input or "reservation" in user_input):
        return "Cancellations made 48+ hours before check-in are fully refunded. Within 48 hours, one night's charge applies."

    elif "room upgrade" in user_input or "upgrade room" in user_input:
        return "Room upgrades are subject to availability at check-in. You can request one at the front desk for a fee."

    # ─── ROOM TYPES & PRICING ────────────────────
    elif "standard room" in user_input:
        return "Standard rooms are $89/night. They include a queen bed, Wi-Fi, and flat-screen TV."

    elif "deluxe room" in user_input:
        return "Deluxe rooms are $149/night. Includes king bed, sea/garden view, mini bar, and premium toiletries."

    elif "suite" in user_input and "price" in user_input:
        return "Our suites start at $299/night and include a living room, jacuzzi, butler service, and panoramic views."

    elif "family room" in user_input:
        return "Family rooms accommodate up to 2 adults and 2 children and are priced at $179/night."

    elif "twin room" in user_input:
        return "Twin rooms with two single beds are available at $99/night. Perfect for colleagues or friends."

    # ─── AMENITIES ───────────────────────────────
    elif "swimming pool" in user_input or "pool" in user_input:
        return "Our rooftop pool is open from 7 AM to 10 PM daily. Towels are provided. Poolside snacks available."

    elif "gym" in user_input or "fitness" in user_input:
        return "The fitness center is open 24/7 and equipped with treadmills, weights, yoga mats, and more."

    elif "spa" in user_input:
        return "Our spa offers massages, facials, and body wraps. Book a session at the concierge. Hours: 9 AM – 8 PM."

    elif "parking" in user_input:
        return "Valet parking is available at $15/day. Self-parking in our secure garage is $10/day."

    elif "wifi" in user_input or "wi-fi" in user_input or "internet" in user_input:
        return "Complimentary high-speed Wi-Fi is available throughout the hotel. Network: GrandHorizon | No password needed."

    # ─── DINING ──────────────────────────────────
    elif "restaurant" in user_input:
        return "We have two restaurants: 'Azure' (fine dining, 7 PM–11 PM) and 'The Terrace' (casual, 7 AM–10 PM)."

    elif "breakfast" in user_input:
        return "Complimentary buffet breakfast is served at The Terrace from 7:00 AM to 10:30 AM daily."

    elif "room service" in user_input:
        return "Room service is available 24/7. Dial extension 101 from your room phone to place an order."

    elif "bar" in user_input or "cocktail" in user_input or "drinks" in user_input:
        return "The Horizon Lounge Bar is open from 4 PM to 1 AM. Happy hour runs from 5–7 PM with 20% off all drinks."

    elif "vegan" in user_input or "vegetarian" in user_input:
        return "Yes! Our restaurants offer a dedicated vegan and vegetarian menu. Just let your server know your preference."

    # ─── SERVICES ────────────────────────────────
    elif "laundry" in user_input or "dry clean" in user_input:
        return "Laundry service is available. Drop your clothes at reception before 9 AM for same-day return."

    elif "concierge" in user_input:
        return "Our concierge desk is at the lobby, open from 7 AM to 11 PM. They can arrange tours, taxis, and more."

    elif "airport shuttle" in user_input or "airport transfer" in user_input:
        return "Airport shuttles are available every 2 hours. Book in advance at the front desk or by calling ext. 105."

    elif "taxi" in user_input or "cab" in user_input:
        return "Our concierge can arrange a taxi for you anytime. Average city-center rate is $20–$30."

    elif "luggage" in user_input or "baggage" in user_input:
        return "Complimentary luggage storage is available at the front desk for early arrivals and late checkouts."

    # ─── HOUSEKEEPING ────────────────────────────
    elif "housekeeping" in user_input or "clean room" in user_input:
        return "Rooms are cleaned daily between 10 AM and 2 PM. For special requests, dial extension 102."

    elif "extra pillow" in user_input or "extra blanket" in user_input:
        return "Extra pillows and blankets are available on request. Please call housekeeping at ext. 102."

    elif "do not disturb" in user_input:
        return "Place the 'Do Not Disturb' sign on your door handle or press the DND button by the room door."

    elif "towel" in user_input:
        return "Fresh towels are delivered daily. For additional towels, call housekeeping at ext. 102 anytime."

    elif "toiletries" in user_input or "shampoo" in user_input or "soap" in user_input:
        return "Standard toiletries are stocked in your room. Premium toiletry kits available on request at the front desk."

    # ─── PAYMENTS & BILLING ──────────────────────
    elif "payment" in user_input or "pay" in user_input:
        return "We accept all major credit/debit cards, UPI, and cash. Contactless payment is preferred at checkout."

    elif "invoice" in user_input or "bill" in user_input or "receipt" in user_input:
        return "A detailed invoice is emailed upon checkout. Request a printed copy at the front desk if needed."

    elif "deposit" in user_input or "security deposit" in user_input:
        return "A refundable security deposit of $100 is collected at check-in and returned within 3–5 business days."

    elif "discount" in user_input or "offer" in user_input or "promo" in user_input:
        return "Check our website for seasonal offers. Members of our loyalty program enjoy up to 20% off."

    elif "loyalty program" in user_input or "rewards" in user_input or "membership" in user_input:
        return "Join our 'Horizon Rewards' loyalty program for free! Earn points on every stay and redeem for free nights."

    # ─── EVENTS & BUSINESS ───────────────────────
    elif "conference" in user_input or "meeting room" in user_input:
        return "We have 4 conference rooms (capacity 10–200 guests) with AV equipment. Contact events@grandhorizon.com."

    elif "wedding" in user_input or "banquet" in user_input:
        return "We host weddings and banquets in our Grand Ballroom (capacity: 500 guests). Call +1-800-EVENTS to inquire."

    elif "birthday" in user_input or "anniversary" in user_input:
        return "We offer celebration packages including cake, flowers, and room decoration. Book via the concierge desk."

    elif "business center" in user_input:
        return "Our business center has printing, scanning, and high-speed internet. Located on Level 2, open 24/7."

    elif "projector" in user_input or "presentation" in user_input:
        return "Projectors and presentation screens are available for meetings. Reserve at least 2 hours in advance."

    # ─── SAFETY & SECURITY ───────────────────────
    elif "lost" in user_input and ("key" in user_input or "card" in user_input):
        return "If you've lost your room key card, go to the front desk immediately. A replacement card costs $5."

    elif "safe" in user_input or "locker" in user_input:
        return "Each room has an in-room digital safe for valuables. Ask front desk if you need assistance."

    elif "emergency" in user_input or "fire" in user_input:
        return "In an emergency, call ext. 0 (front desk) or dial 911."

    elif "security" in user_input:
        return "Our security team patrols the property 24/7 with CCTV active."

    elif "first aid" in user_input or "medical" in user_input or "doctor" in user_input:
        return "First-aid kit available. Doctor can be arranged within 30 minutes."

    # ─── LOCATION & NEARBY ───────────────────────
    elif "address" in user_input or "location" in user_input or "where is" in user_input:
        return "Grand Horizon Hotel is at 42 Oceanview Drive, next to City Central Mall."

    elif "nearby" in user_input or "attraction" in user_input:
        return "Nearby: Museum (1 km), Beach (2 km), Market (0.5 km)."

    elif "shopping" in user_input or "mall" in user_input:
        return "City Central Mall is 2 minutes away."

    elif "transport" in user_input or "bus" in user_input or "train" in user_input:
        return "Metro station 0.3 km away. Bus stop outside hotel."

    elif "weather" in user_input:
        return "Check weather online or ask concierge."

    # ─── GENERAL ─────────────────────────
    elif "pet" in user_input or "dog" in user_input or "cat" in user_input:
        return "Pets allowed up to 10kg for $20/night."

    elif "smoking" in user_input:
        return "Non-smoking property. Designated area available."

    elif "complaint" in user_input:
        return "Please contact front desk. We'll resolve immediately."

    elif "feedback" in user_input:
        return "Leave a review on Google or TripAdvisor."

    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! Welcome to Grand Horizon Hotel. How can I assist you?"

    elif "thank" in user_input:
        return "You're most welcome!"

    elif "help" in user_input:
        return "Ask about rooms, food, services, booking, etc."

    else:
        return "Sorry, I didn't understand that. Type 'help' for options."


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    reply = get_bot_response(user_message)
    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(debug=True)