import tkinter as tk
from tkinter import filedialog, messagebox, Frame, Scrollbar, Text
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Download VADER lexicon (only needs to be done once)
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

dark_mode = False  # Global variable to track dark mode state

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        root.configure(bg='#2E2E2E')
        header_label.config(bg='#555555', fg='white')
        toggle_button.config(bg='#666666', fg='white')
        result_text.config(bg='#333333', fg='white')
        text_frame.config(bg='#2E2E2E')
        pie_chart_frame.config(bg='#2E2E2E')
    else:
        root.configure(bg='#f0f0f0')
        header_label.config(bg='#4CAF50', fg='white')
        toggle_button.config(bg='#008CBA', fg='white')
        result_text.config(bg='white', fg='black')
        text_frame.config(bg='#f0f0f0')
        pie_chart_frame.config(bg='#f0f0f0')

def load_feedback(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'feedback' in df.columns:
            feedback_list = df[['feedback']].dropna().to_dict('records')
            if 'rating' in df.columns:
                feedback_list = df[['feedback', 'rating']].dropna().to_dict('records')
            return feedback_list
        else:
            messagebox.showerror("Error", "CSV file must contain a 'feedback' column.")
            return []
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")
        return []

def generate_improvement_suggestions(feedback):
    suggestion_categories = {
        "slow": ["Optimize processing speed or response time.", "Implement performance enhancements for faster operations."],
        "expensive": ["Review pricing strategies or offer discounts.", "Consider introducing budget-friendly options."],
        "difficult": ["Enhance usability and simplify navigation.", "Provide better user guides or tutorials."],
        "poor": ["Improve quality control and customer support.", "Analyze key issues and work on enhancements."],
        "bad": ["Investigate customer concerns and address common complaints.", "Enhance training programs for staff and service."],
        "broken": ["Ensure proper maintenance and testing to prevent issues.", "Improve product durability and reliability."],
        "complicated": ["Simplify processes and improve user-friendliness.", "Introduce interactive help and better documentation."],
        "unhelpful": ["Improve customer support response time and effectiveness.", "Enhance support team training and knowledge base."],
        "boring": ["Introduce innovative features to keep users engaged.", "Enhance content and make interactions more engaging."],
    }
    
    feedback_lower = feedback.lower()
    suggestions = [suggestion_categories[key] for key in suggestion_categories if key in feedback_lower]
    
    if suggestions:
        return random.choice(random.choice(suggestions))
    return "Consider gathering more customer insights to improve the experience."

def analyze_feedback(feedback_list):
    results = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for item in feedback_list:
        feedback = item['feedback']
        rating = item.get('rating', 'N/A')
        score = sia.polarity_scores(str(feedback))['compound']
        sentiment = "Neutral"
        suggestion = ""
        if score >= 0.05:
            sentiment = "Positive"
            sentiment_counts["Positive"] += 1
        elif score <= -0.05:
            sentiment = "Negative"
            sentiment_counts["Negative"] += 1
            suggestion = generate_improvement_suggestions(feedback)
        else:
            sentiment = "Neutral"
            sentiment_counts["Neutral"] += 1
        results.append((feedback, rating, sentiment, suggestion))
    
    return results, sentiment_counts

def plot_pie_chart(sentiment_counts, frame):
    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())
    colors = ['green', 'red', 'gray']
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def simulate_business_improvement():
    messagebox.showinfo("Business Improvement Simulation", "Businesses can leverage sentiment insights to improve customer satisfaction by:\n\n- Addressing common negative feedback trends proactively.\n- Implementing AI-driven chatbots for real-time support.\n- Setting up automated alerts for immediate issue resolution.")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        feedback_list = load_feedback(file_path)
        if feedback_list:
            results, sentiment_counts = analyze_feedback(feedback_list)
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            for fb, rating, sent, suggestion in results:
                result_text.insert(tk.END, f"Review: {fb}\nRating: {rating}\nSentiment: {sent}\n")
                if sent == "Negative":
                    result_text.insert(tk.END, f"Suggested Improvement: {suggestion}\n\n", "red")
                else:
                    result_text.insert(tk.END, "\n")
            result_text.config(state=tk.DISABLED)
            plot_pie_chart(sentiment_counts, pie_chart_frame)

# GUI setup remains unchanged
root = tk.Tk()
root.title("AI-Driven Customer Feedback Analysis")
root.geometry("700x800")
root.configure(bg='#f0f0f0')

header_label = tk.Label(root, text="AI-Driven Customer Feedback Analysis", font=("Arial", 14), bg='#4CAF50', fg='white')
header_label.pack(pady=10, fill=tk.X)

toggle_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode, bg='#008CBA', fg='white', font=("Arial", 10), padx=10, pady=5)
toggle_button.pack(pady=5)

tk.Button(root, text="Load Feedback File", command=open_file, bg='#008CBA', fg='white', font=("Arial", 10), padx=10, pady=5).pack(pady=5)
tk.Button(root, text="Simulate Business Improvement", command=simulate_business_improvement, bg='#FFA500', fg='white', font=("Arial", 10), padx=10, pady=5).pack(pady=5)

text_frame = Frame(root, bg='#f0f0f0')
text_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = Text(text_frame, font=("Arial", 12), wrap=tk.WORD, yscrollcommand=scrollbar.set, height=10, bg='white', fg='black')
result_text.pack(fill=tk.BOTH, expand=True)
result_text.config(state=tk.DISABLED)
scrollbar.config(command=result_text.yview)
result_text.tag_configure("red", foreground="red")

pie_chart_frame = Frame(root, bg='#f0f0f0')
pie_chart_frame.pack(pady=20)

root.mainloop()
