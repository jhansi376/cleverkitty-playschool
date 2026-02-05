import os

file_path = r"c:\Users\jhans\Downloads\playschool\about\our-team.html"

new_footer = """    <!-- FOOTER: V2 "Enchanted Garden" -->
    <footer class="bg-emerald-950 text-emerald-100/80 py-24 relative overflow-hidden font-sans">
        <!-- Grass Top Divider -->
        <div class="absolute top-0 left-0 w-full overflow-hidden leading-none z-20">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"
                preserveAspectRatio="none" class="relative block w-full h-16 fill-white">
                <path
                    d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z">
                </path>
            </svg>
        </div>

        <!-- Fireflies -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <div
                class="absolute top-1/4 left-1/4 w-1 h-1 bg-yellow-400 rounded-full animate-float opacity-40 shadow-[0_0_10px_rgba(250,204,21,0.8)]">
            </div>
            <div
                class="absolute top-3/4 right-1/3 w-1.5 h-1.5 bg-yellow-400 rounded-full animate-float delay-700 opacity-60 shadow-[0_0_15px_rgba(250,204,21,0.8)]">
            </div>
            <div
                class="absolute top-1/3 right-10 w-2 h-2 bg-yellow-400 rounded-full animate-wiggle delay-1000 opacity-30 shadow-[0_0_20px_rgba(250,204,21,0.8)]">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 relative z-10 pt-12">
            <div class="grid md:grid-cols-4 gap-12 mb-16">
                <!-- Col 1: Brand & Newsletter -->
                <div class="md:col-span-1 space-y-6">
                    <div class="flex items-center gap-3">
                        <span class="text-4xl filter drop-shadow-lg">🍃</span>
                        <h4 class="text-3xl font-bold font-hand text-white">CleverKitty</h4>
                    </div>
                    <p class="text-sm leading-relaxed text-emerald-200/70">
                        Nurturing curiosity in our enchanted garden of learning. Where every day is a new discovery.
                    </p>

                    <!-- Integrated Newsletter -->
                    <div class="bg-white/5 backdrop-blur-sm p-4 rounded-2xl border border-white/10 mt-6">
                        <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider mb-2">Join our
                            Story</label>
                        <div class="flex gap-2">
                            <input type="email" placeholder="Email..."
                                class="bg-white/10 border-none rounded-lg px-3 py-2 text-sm text-white placeholder-emerald-400/50 w-full focus:ring-1 focus:ring-amber-300 outline-none">
                            <button
                                class="bg-amber-400 text-emerald-900 rounded-lg p-2 hover:bg-amber-300 transition shadow-lg hover:shadow-amber-400/20">
                                <i data-lucide="arrow-right" class="w-4 h-4"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Col 2: Programs -->
                <div>
                    <h4 class="text-white font-bold text-lg mb-6 flex items-center gap-2"><i data-lucide="sprout"
                            class="w-4 h-4 text-emerald-400"></i> Programs</h4>
                    <ul class="space-y-4 text-sm font-medium">
                        <li><a href="../classes/play-group.html"
                                class="hover:text-amber-300 transition flex items-center gap-2 group"><span
                                    class="w-1.5 h-1.5 bg-emerald-600 rounded-full group-hover:bg-amber-300 transition"></span>
                                Play Group</a></li>
                        <li><a href="../classes/nursery.html"
                                class="hover:text-amber-300 transition flex items-center gap-2 group"><span
                                    class="w-1.5 h-1.5 bg-emerald-600 rounded-full group-hover:bg-amber-300 transition"></span>
                                Nursery</a></li>
                        <li><a href="../classes/kindergarten.html"
                                class="hover:text-amber-300 transition flex items-center gap-2 group"><span
                                    class="w-1.5 h-1.5 bg-emerald-600 rounded-full group-hover:bg-amber-300 transition"></span>
                                Kindergarten</a></li>
                    </ul>
                </div>

                <!-- Col 3: Quick Links -->
                <div>
                    <h4 class="text-white font-bold text-lg mb-6 flex items-center gap-2"><i data-lucide="compass"
                            class="w-4 h-4 text-sky-400"></i> Quick Links</h4>
                    <ul class="space-y-4 text-sm font-medium">
                        <li><a href="../index.html" class="hover:text-amber-300 transition block">Home</a></li>
                        <li><a href="../about.html" class="hover:text-amber-300 transition block">About</a></li>
                        <li><a href="../about/our-team.html" class="hover:text-amber-300 transition block">Our Team</a>
                        </li>
                        <li><a href="../about/gallery.html" class="hover:text-amber-300 transition block">Gallery</a></li>
                        <li><a href="../about/blog.html" class="hover:text-amber-300 transition block">Blog</a></li>

                    </ul>
                </div>

                <!-- Col 4: Contact -->
                <div>
                    <h4 class="text-white font-bold text-lg mb-6 flex items-center gap-2"><i data-lucide="map-pin"
                            class="w-4 h-4 text-rose-400"></i> Visit Us</h4>
                    <address class="not-italic text-sm space-y-4">
                        <p class="flex items-start gap-3">
                            <span class="mt-1">📍</span>
                            <span>123 Sunshine Lane,<br>Happy Valley, AP - 530003</span>
                        </p>
                        <p class="flex items-center gap-3">
                            <span>📞</span>
                            <a href="tel:+919876543210" class="font-bold text-amber-300 hover:text-white transition">+91
                                98765 43210</a>
                        </p>
                        <p class="flex items-center gap-3">
                            <span>💌</span>
                            <a href="mailto:hello@cleverkitty.com"
                                class="hover:text-white transition">hello@cleverkitty.com</a>
                        </p>
                        <!-- Socials -->
                        <div class="flex gap-4 mt-6">
                            <a href="#"
                                class="w-10 h-10 bg-white/5 rounded-full flex items-center justify-center hover:bg-blue-600 transition hover:-translate-y-1"><i
                                    data-lucide="facebook" class="w-5 h-5"></i></a>
                            <a href="#"
                                class="w-10 h-10 bg-white/5 rounded-full flex items-center justify-center hover:bg-rose-600 transition hover:-translate-y-1"><i
                                    data-lucide="instagram" class="w-5 h-5"></i></a>
                            <a href="#"
                                class="w-10 h-10 bg-white/5 rounded-full flex items-center justify-center hover:bg-red-600 transition hover:-translate-y-1"><i
                                    data-lucide="youtube" class="w-5 h-5"></i></a>
                            <a href="#"
                                class="w-10 h-10 bg-white/5 rounded-full flex items-center justify-center hover:bg-sky-500 transition hover:-translate-y-1"><i
                                    data-lucide="twitter" class="w-5 h-5"></i></a>
                        </div>
                    </address>
                </div>
            </div>

            <!-- Bottom Bar -->
            <div
                class="border-t border-emerald-900 pt-8 text-center text-xs text-emerald-600 flex flex-col md:flex-row justify-between items-center gap-4">
                <p>&copy; 2024 CleverKitty Play School. Growing with love.</p>
                <div class="flex gap-6">
                    <a href="#" class="hover:text-emerald-400">Privacy Policy</a>
                    <a href="#" class="hover:text-emerald-400">Terms of Use</a>
                </div>
            </div>
        </div>
    </footer>"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "<!-- FOOTER -->"
end_marker = "</footer>"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find start marker")
    exit(1)

# Find the CLOSING tag of the footer, searching from the start marker
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print("Could not find end marker")
    exit(1)

# Include the closing tag in the replacement range
end_idx += len(end_marker)

# Construct the new content
updated_content = content[:start_idx] + new_footer + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"Successfully updated footer in {file_path}")
