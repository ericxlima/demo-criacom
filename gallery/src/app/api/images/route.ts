import { storage } from "@/lib/firebase";
import { v4 as uuidv4 } from "uuid";
import { db as prisma } from "@/lib/prisma";
import { NextResponse } from "next/server";

export async function GET() {
    try {
        const images = await prisma.images.findMany();

        return NextResponse.json({ images }, { status: 200 });
    } catch (error) {
        return new Response(JSON.stringify({ message: 'Internal error', error: error }), {
            status: 500
        });
    }
}

export async function POST(req: Request) {
    try {
        const contentType = req.headers.get('content-type') || '';

        if (!contentType.includes('multipart/form-data')) {
            return new Response(JSON.stringify({ error: 'Invalid content-type' }), {
                status: 400
            });
        }

        const formData = await req.formData();

        const file = formData.get('file') as File | null;
        const userId = formData.get('userId') as string;

        if (!file || !userId) {
            return new Response(JSON.stringify({ error: 'Missing file or user ID' }), {
                status: 400
            });
        }

        const arrayBuffer = await file.arrayBuffer();
        const buffer = Buffer.from(arrayBuffer);

        // Read the file and upload to Firebase Storage
        const destinationFileName = `user-${userId}/${uuidv4()}_${file.name}`;

        const fileInBucket = storage.file(destinationFileName);

        await fileInBucket.save(buffer, {
            contentType: file.type,
            public: true, // Make the file publicly accessible
        })

        const publicUrl = `https://storage.googleapis.com/${storage.name}/${destinationFileName}`;

        await prisma.images.create({
            data: {
                name: file.name || "unknown", // Save original file name
                imageUrl: publicUrl, // URL to the uploaded file in Firebase Storage
            },
        })

        return NextResponse.json({ url: publicUrl }, { status: 200 });
    } catch (error) {
        console.log(error)
        return new Response(JSON.stringify({ error: "File upload failed", details: error }), {
            status: 500
        });
    }
};