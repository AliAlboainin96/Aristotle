#[allow(non_snake_case)]

use std::fs::File;
use std::fs;
use std::io::prelude::*;
use std::io::Write;
use std::path::*;

use simple_xml_builder::XMLElement;

pub fn increament(num: &mut i32) {
    *num +=1;
}

pub struct Book {
    pub ASIN: String,
    pub Title: String,
    pub Author: String,
    pub Genre: String
}

impl Book {
    
    fn bookEntry(&self) -> Result<(), std::io::Error> {

        let mut ID = 0;

        let mut outXMLFile = fs::OpenOptions::new()
            .append(true)
            .create(true)
            .open("lib.xml")
            .unwrap();

        let mut temp_book = XMLElement::new("Book");
        temp_book.add_attribute("ID", ID);
        increament(&mut ID);

        let mut temp_asin = XMLElement::new("ASIN");
        temp_asin.add_text(&self.ASIN);
        temp_book.add_child(temp_asin);


        let mut temp_title = XMLElement::new("Title");
        temp_title.add_text(&self.Title);
        temp_book.add_child(temp_title);

       let mut temp_author= XMLElement::new("Author");
        temp_author.add_text(&self.Author);
        temp_book.add_child(temp_author);

       let mut temp_genre = XMLElement::new("Genre");
        temp_genre.add_text(&self.Genre);
        temp_book.add_child(temp_genre);


        temp_book.write(outXMLFile)?;
        

        println!("{}",ID);
        Ok(())
        }
}

fn main() {

    let mut book1 = Book {
        ASIN: String::from("101001010"),
        Title: String::from("Crime and Punishment"),
        Author: String::from("Fyod"),
        Genre: String::from("Non-Fiction"),
    };

    let mut book2 = Book {
        ASIN: String::from("433545454"),
        Title: String::from("Crime but not cratee"),
        Author: String::from("Mohm"),
        Genre: String::from("yes-fiction"),
    };

    //book1.bookEntry();
    book2.bookEntry(); 
}



