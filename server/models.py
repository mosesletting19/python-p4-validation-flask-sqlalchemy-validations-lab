from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        assert len(phone_number) == 10, "Phone number must be exactly ten digits."
        return phone_number
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def validate_content(self, key, content):
        assert len(content) >= 250, "Post content must be at least 250 characters long."
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        assert len(summary) <= 250, "Post summary must be a maximum of 250 characters long."
        return summary

    @validates('category')
    def validate_category(self, key, category):
        assert category in ['Fiction', 'Non-Fiction'], "Post category must be either Fiction or Non-Fiction."
        return category

    @validates('title')
    def validate_title(self, key, title):
        assert any(word in title for word in ["Won't Believe", "Secret", "Top", "Guess"]), \
            "Post title must contain one of the following: 'Won't Believe', 'Secret', 'Top', 'Guess'"
        return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
