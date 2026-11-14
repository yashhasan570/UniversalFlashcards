// Copyright: Universal Flashcards Software, LLC and contributors
// License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
use std::env;
use std::process;

use universalflashcards::log::set_global_logger;
use universalflashcards::sync::http_server::SimpleServer;

fn main() {
    if let Some(arg) = env::args().nth(1) {
        if arg == "--healthcheck" {
            run_health_check();
            return;
        }
    }
    if env::var("RUST_LOG").is_err() {
        env::set_var("RUST_LOG", "universalflashcards=info")
    }
    set_global_logger(None).unwrap();
    println!("{}", SimpleServer::run());
}

fn run_health_check() {
    if SimpleServer::is_running() {
        process::exit(0);
    } else {
        process::exit(1);
    }
}
