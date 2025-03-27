import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import { FaLinkedin } from "react-icons/fa";

const TestimonialSlider = () => {
  const [testimonials, setTestimonials] = useState([]);
  const [selectedTestimonial, setSelectedTestimonial] = useState(null);
  const [loading, setLoading] = useState(true);

  async function fetchTestimonials() {
    try {
      const response = await fetch("https://api.projectdevops.in/testimonials");
      const data = await response.json();
      if (data && Array.isArray(data)) {
        setTestimonials(data);
      } else {
        console.log("No testimonials found!");
      }
    } catch (err) {
      console.log("Error fetching testimonials: ", err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchTestimonials();
  }, []);

  if (loading) {
    return <p className="text-center text-xl mt-10">Loading testimonials...</p>;
  }

  if (testimonials.length === 0) {
    return <p className="text-center text-xl mt-10">No testimonials available.</p>;
  }

  return (
    <div className="overflow-hidden w-full py-10 bg-gray-100">
      <h2 className="text-center text-3xl font-bold mb-8">Testimonials</h2>

      <motion.div
        className="flex gap-6"
        animate={{ x: [0, -testimonials.length * 250] }} // Adjusting motion x dynamically
        transition={{ repeat: Infinity, duration: testimonials.length * 5, ease: "linear" }}
        style={{ display: "flex", flexWrap: "nowrap", width: `${testimonials.length * 100}%` }}
      >
        {testimonials.map((testimonial, index) => (
          <div
            key={index}
            className="min-w-[70vw] md:min-w-[45vw] lg:min-w-[30vw] max-w-[400px] bg-white shadow-xl p-6 rounded-2xl flex flex-col items-center text-center cursor-pointer"
            onClick={() => setSelectedTestimonial(testimonial)}
          >
            <img
              src={testimonial.image_url || "https://via.placeholder.com/150"}
              alt={testimonial.name}
              className="w-20 h-20 rounded-full object-cover mb-3"
            />
            <h3 className="text-lg font-semibold">{testimonial.name}</h3>
            <p className="text-gray-700 mt-3 text-sm sm:text-base leading-relaxed">
              {testimonial.content.length > 80
                ? testimonial.content.slice(0, 80) + "..."
                : testimonial.content}
            </p>
            {testimonial.linkedin && (
              <a
                href={testimonial.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="mt-3 text-blue-500 hover:text-blue-700 flex items-center gap-2"
              >
                <FaLinkedin size={20} /> Connect
              </a>
            )}
          </div>
        ))}
      </motion.div>

      {/* POPUP MODAL */}
      {selectedTestimonial && (
        <motion.div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={() => setSelectedTestimonial(null)}
        >
          <motion.div
            className="bg-white p-6 rounded-2xl shadow-lg w-[85%] md:w-[50%] lg:w-[35%] text-center relative flex justify-center items-center flex-col"
            initial={{ scale: 0.8 }}
            animate={{ scale: 1 }}
            exit={{ scale: 0.8 }}
            onClick={(e) => e.stopPropagation()} // Prevents closing when clicking inside the modal
          >
            <button
              className="absolute top-3 right-3 text-gray-500 hover:text-gray-700 text-2xl"
              onClick={() => setSelectedTestimonial(null)}
            >
              &times;
            </button>
            <img
              src={selectedTestimonial.image_url || "https://via.placeholder.com/150"}
              alt={selectedTestimonial.name}
              className="w-20 h-20 rounded-full object-cover mb-3 mx-auto"
            />
            <h3 className="text-lg font-semibold">{selectedTestimonial.name}</h3>
            <p className="text-gray-700 mt-3 text-sm sm:text-base leading-relaxed">
              {selectedTestimonial.content}
            </p>
            {selectedTestimonial.linkedin && (
              <a
                href={selectedTestimonial.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="mt-3 inline-block text-blue-500 hover:text-blue-700 flex items-center gap-2"
              >
                <FaLinkedin size={20} /> Connect
              </a>
            )}
          </motion.div>
        </motion.div>
      )}
    </div>
  );
};

export default TestimonialSlider;