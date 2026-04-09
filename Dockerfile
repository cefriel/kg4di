FROM jbangdev/jbang

WORKDIR /app

# Ensure non-interactive mode
ENV JBANG_TRUST_ALL=true

# Pre-install Camel and trust the source
RUN jbang trust add https://github.com/apache/camel/ \
 && jbang app install camel@apache/camel

# Copy Java helper
COPY GeoFunctions.java /app/GeoFunctions.java

# Pre-fetch the mapping-template dependency into jbang's cache
RUN printf '//DEPS com.cefriel:camel-chimera-mapping-template:4.6.0\nclass Warmup { public static void main(String[] a) {} }\n' > /tmp/Warmup.java \
 && jbang build /tmp/Warmup.java \
 && rm /tmp/Warmup.java

# Reset ENTRYPOINT inherited from jbangdev/jbang (which is ["jbang"]),
# otherwise shell-form CMD gets passed as arguments to jbang.
ENTRYPOINT []

# Default command (use shell form to allow glob expansion)
CMD jbang --java-options="-Dhttp.agent=MyCustomAgent/1.0" camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0 GeoFunctions.java
